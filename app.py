import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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
    gigs = list(mongo.db.gigs.find())
    return render_template("index.html", gigs=gigs)


@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    gigs = list(mongo.db.gigs.find({"$text": {"$search": search}}))
    return render_template("all_gigs.html", gigs=gigs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username is already in use")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("fname").lower(),
            "last_name": request.form.get("lname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have registered successfully!")
        return redirect(url_for("all_gigs", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "all_gigs", username=session["user"]))
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
        return redirect(url_for("all_gigs"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_gig.html", categories=categories)


@app.route("/edit_gig/<gig_id>", methods=["GET", "POST"])
def edit_gig(gig_id):
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

    gig = mongo.db.gigs.find_one({"_id": ObjectId(gig_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_gig.html", gig=gig, categories=categories)


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("all_gigs"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)