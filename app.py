import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, \
    PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, \
    EqualTo, Length
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/all_gigs")
def all_gigs():
    """
    Renders home page review cards from DB
    """
    gigs = list(mongo.db.gigs.find())
    return render_template("index.html", gigs=gigs)


@app.route("/profile")
def profile():
    """
    Renders profile page review cards from DB
    """
    gigs = list(mongo.db.gigs.find())
    return render_template("profile.html", gigs=gigs)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    This function is meant to allow the user to search for
    specific artist or gig. I can't however get it to work
    correctly. I will keep the function in while I work on
    it. I have added the search.html to gitignore file until
    it is ready to deploy.
    """
    query = request.form.get("search")
    gigs = list(mongo.db.gigs.find({"$text": {"$search": query}}))
    return render_template("index.html", gigs=gigs)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    function allows the user to sign up to the website with a
    first and last name, username and password. They will get
    a prompt when registration is successful and will be
    redirected to their profile page.
    """

    class CreateUserForm(FlaskForm):
        """
        This Class is the registration form which will validate
        all fields and also verify the password matches in both
        fields
        """

        fname = StringField(
            label=('First Name'),
            validators=[DataRequired()]
        )

        lname = StringField(
            label=('Last Name'),
            validators=[DataRequired()]
        )

        username = StringField(
            label=('Username'),
            validators=[DataRequired(),
                        Length(max=24)]
        )

        password = PasswordField(
            label=('Password'),
            validators=[DataRequired(),
                        Length(
                            min=6,
                            message='Your Password should be at least %(min)\
                                 characters long'
                            )
                        ]
        )

        confirmpassword = PasswordField(
            label=('Confirm Password'),
            validators=[DataRequired(message='*Required Field'),
                        EqualTo(
                            'password',
                            message='Both Password Fields Must Match!'
                            )
                        ]
        )

        submit = SubmitField(
            label=('Sign Up')
        )

    form = CreateUserForm(request.form)

    if request.method == "POST" and form.validate():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username is already in use")
            return redirect(url_for("register"))

        registerdata = {
            "first_name": form.fname.data.lower(),
            "last_name": form.lname.data.lower(),
            "username": form.username.data.lower(),
            "password": generate_password_hash(
                form.confirmpassword.data
                )
        }

        mongo.db.users.insert_one(registerdata)

        session["user"] = request.form.get("username").lower()
        flash("You have registered successfully!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    User can log in using credentials they have already submitted to the
    database. They will be redirected to their profile page once
    logged in
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/add_gig", methods=["GET", "POST"])
def add_gig():
    """
    This function is allows the user to add a gig to the database, they will
    also get a prompt when the gig is added successfully
    """
    if request.method == "POST":
        gig = {
            "category_name": request.form.get("category_name"),
            "band_name": request.form.get("band_name"),
            "where": request.form.get("where"),
            "when": request.form.get("when"),
            "description": request.form.get("review"),
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.gigs.insert_one(gig)
        flash("Gig added Successfully!")
        return redirect(url_for("profile"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_gig.html", categories=categories)


@app.route("/edit_gig/<gig_id>", methods=["GET", "POST"])
def edit_gig(gig_id):
    """
    Function allows user to edit gigs with the values they
    have already submitted to the database
    """
    if request.method == "POST":
        gig_edit = {
            "category_name": request.form.get("category_name"),
            "band_name": request.form.get("band_name"),
            "where": request.form.get("where"),
            "when": request.form.get("when"),
            "description": request.form.get("review"),
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.gigs.update({"_id": ObjectId(gig_id)}, gig_edit)
        flash("You have successfully updated your gig!")
        return redirect(url_for("profile"))

    gig = mongo.db.gigs.find_one({"_id": ObjectId(gig_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_gig.html", gig=gig, categories=categories)


@app.route("/delete/<gigs_id>")
def delete(gigs_id):
    """
    Allows user to delete gigs from database
    """
    mongo.db.gigs.remove({"_id": ObjectId(gigs_id)})
    flash("You have deleted the gig successfully!")
    return redirect(url_for("profile"))


@app.route("/logout")
def logout():
    """
    Allows user to logout and delete session cookie.
    This way other users can sign in to access their
    gigs
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("all_gigs"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
