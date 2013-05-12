Pre Caffine Bike Status
==============

This is just a quick bodge so I know which bike station to walk to or park up at.
The idea of this is to be really simple, so I don't have to think about maps and all that complicated shit when I'm half asleep!

# Make your own
As you can tell I live in Tower Hamlets, if you for some reason do not, clone this and change the `STATION_IDS` in **data.py** to 3 that are near you, or whatever you're interested in.

    STATION_IDS = [200, 33, 489]

Make a Heroku project

    heroku create

You will need to sign up to access the TFL API here http://www.tfl.gov.uk/businessandpartners/syndication/16492.aspx
The will give you the API URL with your email address in it, you will have to add that to the Heroku config

    heroku config:set TFL_EMAIL={your email}

Commit your changes and push it up
    
    git push heroku master
    heroku ps:scale web=1
