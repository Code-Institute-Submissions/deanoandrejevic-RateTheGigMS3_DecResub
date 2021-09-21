# Rate The Gig MS3

Rate the Gig is a platform where you can come and rate the gigs you've been too and schedule gigs you're going too!

![Image of live website through Am I Responsive](/static/readme/am-i-responsive-ms3.png)

[Link to live website](http://rate-the-gig-ms3.herokuapp.com/all_gigs)

# User Experience (UX)

You are thrown straight into the front page! Greeted by the hero image and a welcome message. I have been sure to add alt tags to as much as possible
so even people with disibilities can use the site too! 

### First Time User

1. I want to be able to easily view gigs by either searching or scrolling through.
2. I want to be able to register an account with a username and password of my choosing
3. I would like to be able to log out after I am done.

### Regular User

1. I would like to able to visit the page and login using my previous username and password 
2. Once I am in I want to be able to add reviews as I see fit.
3. When I have added said reviews I want to be able view only my reviews under a dedicated page!
4. When I am in my profile page, I would like to be able to add new gig reviews and edit reviews too.
5. I would also like to delete my reviews too.
6. When I have done any of these tasks, I would like on screen feedback when they have been successfully.
7. I would like to be able to log out after I am done.

## The Scope

1. I want people to be able to find gig reviews related to a band they want to see.
2. I want people to able to add reviews to the site, so every one can see them.
3. I want people who are signing into the site to able to schedule reviews so that they can be updated later for everyone to see.
4. I want people to be able to view reviews that they have added on a dedicated page and from this page, edit and delete.

## Structure

The structure of project is almost excatly as intended. I have an easy to understand navigation bar which collapses in mobile view to a hamburger icon. It has a welcome back which greets the user and also tells them directly if they want to add reviews they have to sign up. Below is where the review cards  are stored. The user will be able to see all gig review cards and will have the ability to search through them. The users will able to navigate to a profile page, once they have logged in, where they can view all of their cards.

# Features

### Implemented

1. Reviews cards are easily viewable when scrolling down, the more gigs that get added the more cards are viewable to everyone.
2. Able to sign up straight from the welcome box.
3. Nav bar hides certain elements when user is not signed in
4. User can register with Name, Username and password.
5. Once user has registered, they can freely log out and log in.
6. When user creates an account and logs out of their account they will get a prompt saying they have done so.
7. A user can navigate to their profile page where they can view they can veiw all their review cards and only their review cards.
8. When a user is signed in they can then add gig cards by filling out a form. Within this form they can select, Attended or Upcoming. If they select "upcoming" only that user can view that review card.
9. The user can also edit their own review cards. When they have attended a gig they change the Upcoming category to Attended which will make it veiwable to all users, regardless of whether they are signed in or not.
10. I have added an Admin user too which has master access over everything and can delete, edit and add gig cards regardless of who created review cards. You can log in to said account using. Username: `__admin__` Password: `__admin__`

### To be implemented

1. I would like to add the ability to search for gig cards, whether that be by artist name, venue etc.. This feature is currently a work in progress, as I cant seem to get it too work correctly. The search feature and html page is currently in the gitignore file so I can't deploy by accident.
2. I would like to add a feature that sends out an email once the user has signed up. I have installed Flask_Mail where I did try to implement said email. I think it started to work as I was getting sign in security notifications from google, but it was never sending the email. This is something that can be added in later as my knowledge expands.



## Wireframes

 
- ![Home_Page](/static/readme/Home-Page-Wireframe.png)


# Testing

HTML Validator
- ![HTML]()

CSS Validator
- ![CSS](/static/readme/MS3-CSS-Validator.PNG)

Python PEP 8 Compliance
- ![Python_PEP8](/static/readme/PEP8-Compliance.PNG)

## Device Testing
I have tested on the following devices

- Windows Desktop with a 4k, 2k and 1080p display
- Google Pixel 4 XL
- Samsung Galaxy S20 Note Ultra
- Samsung Galaxy S21 Ultra
- iPhone 12 Pro
- iPhone 12 Pro Max
- iPhone 11 Pro
- Google Chromebook
- Lenovo Tab P11
- Moto G 5G Plus
- Amazon Fire Tablet 10"

No Reported Issues on these devices

## Testing Functions

- *all_gigs()* : This function displays all review cards within the index page. Works fine!

- *profile()* : This function displays all review cards within the profile page. Works fine!

- *search()* : This function allows users to search for review cards within the home page. Still a work in progress!

- *register()* : This function allows the user to register an account. Works fine!

- *login()* : This function allows the user to login to their account. Works fine!

- *add_gig()* : This function allows the user to add review cards for everyone to see. Works fine!

- *edit_gig()* : This function allows the user to edit gig review cards that they have created. This also allows them to make viewable to everyone or just themselves. Works fine!

- *delete()* : This function allows the user to delete review cards that they have created. Works fine!

- *logout()* : This function allows the user to log out. It does this by deleting the session cookie, which then in turn allows the user to sign in again. Works fine!

### Bugs

I am currently experiencing a bug where the wrong review card is being deleted. If I select the delete button on one of the cards it will always delete the first review card on the list. The issue started when I added a confirmation Modal to the app. I would assume that this is the issue, but I want to iron it out so I can keep the Modal and it delete the correct review card.

*UPDATE FIXED**

The issue with the deletion was the modal. I have removed the modal for now until I find a solution to fix it properly. I have reached out for help but haven't got the time to implement it right now.

# Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CCS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libaries, Frameworks

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [MongoDB](https://www.mongodb.com/)
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
- [Materialize CSS](https://materializecss.com/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [Google Fonts](https://fonts.google.com/) Staatliches and Open Sans fonts used.
- [Balsamiq](https://balsamiq.com/) Balsamiq was used to make my wireframes and general design of my website.

### Version Control
- [GitHub](https://github.com/) GitHub was used for storage of code and deployment of page via GitHub Pages.
- [GitPod](https://www.gitpod.io/) GitPod was used as the primary editor and also to push and commit my code.

### Other:
- [Google Dev Tools](https://developer.chrome.com/docs/devtools/) Google Chrome Dev Tools was a huge help in discovering bugs and figuring out the solution before actually commiting it to my own code.

- [Code Institute](https://codeinstitute.net/) The Code Institute is where all my current coding knowledge has come from.

# Deployment

This project was deployed to Heroku with the following steps:

1. Ensure your app has debug mode set to False when deploying.
2. Add a file called `Procfile` with no extension to your project directory and add `web: python app.py`
3. Heroku can install dependencies from a requirements.txt or a Pipfile
   - To create a requirements.txt run `pip freeze > requirements.txt`
4. Create an account on Heroku and create a new app.
5. In your app dashboard, in the deploy section, select 'Connect to GitHub'
6. Select the GitHub repository that contains your project.
7. Select Automatic deploys and choose your desired branch.
8. Go to the app settings on Heroku and click 'Reveal Config Vars'
9. Add the required keys as they are in your local env.py (i.e IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME)
10. Go to the app Overview page and when the build is finished, click 'Open App'

# Credits

## Images
- The home image used was from [Unsplash](https://unsplash.com/photos/NMx_9N2QC5o)
- The profile image used was from [Unsplash](https://unsplash.com/photos/RAZQiZOX3mU)

## Code
- The Python code was heavily inspired by the Task Manager Mini Project done by the Code Institue, I have tweaked it and added stuff as needed.
- [Flask_Mail](https://pythonhosted.org/Flask-Mail/) Is a technology that I wanted to implement into my code but I couldn't get it done in the end, but it helped me massively in my understanding of Python code.

## Acknowledgements
I would like to thank a bunch of friends and family
- Megan Cox
- Ben Holloway
- Jack Andersen
- Will Massey
- Callum Guy
- Luke Munsch
- Ella Fitzgerald
- Darren Stevenson (Step-Dad)
- Daniella Stevenson (Mum)
- These guys all helped me in finding issues in my website and breaking my site to help flush out bugs in my code.

I would also like to thank the Code Insititue for helping me expand my knowledge on Python coding and further practices.

