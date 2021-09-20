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
10. I have added an Admin user too which has master access over everything and can delete, edit and add gig cards regardless of who created review cards.

### To be implemented

1. I would like to add the ability to search for gig cards, whether that be by artist name, venue etc.. This feature is currently a work in progress, as I cant seem to get it too work correctly. The search feature and html page is currently in the gitignore file so I can't deploy by accident.
2. I would like to add a feature that sends out an email once the user has signed up. I have installed Flask_Mail where I did try to implement said email. I think it started to work as I was getting sign in security notifications from google, but it was never sending the email. This is something that can be added in later as my knowledge expands.
3. 



## Wireframes

__Home Page__ [Home_Page]()
__Profile Page__ [Profile_Page]()

