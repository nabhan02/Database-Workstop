# Database-Workstop

Today we'll go over how to set up a database using Flask and Flask-SQLAlchemy and connect it to a simple web app. Before we begin, clone this repository into a local directory that you want to use for this project. Also, make sure you have the latest versions of Python and virtualenv installed. If you haven't downloaded them yet, you can visit this link for Python: https://www.python.org/downloads/ and follow the instructions below for virtualenv.

## Installing Virtualenv

Run this command in your terminal to install virtualenv:
    
    pip install virtualenv

## Installing Flask and Flask-SQLAlchemy

1. Open your terminal and create a virtual environment. We want to install dependencies in a virtual environment because different projects that you may be working on might require different versions of the dependencies that you're using. Using a virtual environment ensures that you always have the right dependencies for your current project. Run the following command to create your virtual environment.

    For macOS/Linux:
    ~~~
    python3 -m venv venv
    ~~~
    For Windows:
    ~~~
    py -3 -m venv venv
    ~~~
2. Then, activate your virtual environment:

    For macOS/Linux:
    ~~~
    . venv/bin/activate
    ~~~
    For Windows:
    ~~~
    venv\Scripts\activate
    ~~~
3. Finally, run the following lines to install Flask and Flask-SQLAlchemy using pip:
    ~~~
    pip install Flask
    pip install -U Flask-SQLAlchemy
    ~~~

## Creating a Basic Web App

1. Take a look at the files in your directory, `starter.py` and the `templates` and `static` folders. 
    
    `starter.py` contains a basic Flask application that creates a simple database and displays the content and formatting from `templates` and `static`.
2. Now let's take a look at our rudimentary web app. From your project directory, run the following command and go to `localhost:5000` to take a look:
    
    For macOS/Linux:
    ~~~
    python3 starter.py
    ~~~
    For Windows:
    ~~~
    py starter.py
    ~~~
    If you try to add any groceries, you'll see that you get an error. Before using the grocery list, the functions in `starter.py` must be fully implemented.
3. Now take a closer look at `starter.py`. This file includes several imports and defines a Flask app, SQL database, `Grocery` class, and several functions for the grocery list. Start fixing the web app by filling in the blanks for the imcomplete functions.
4. First, implement the post request in the `index` function. In this function, you need to capture the input from the user-submitted form and make a grocery object out of the submitted info.
    
    Add the grocery item to the update (similar to how you would stage a git commit).
    
    Then, commit that change to the database and redirect back to the homepage of the web app.
5. Next, implement the delete function. 
    
    This function gets an element from the database and deletes it from the database (HINT: think about how to identify items on the list without using its name).
    
    Then commit your changes and redirect back to the homepage, just like you did in the previous function.
6. Finally, implement the update function.

    Using what you've learned from the previous two functions, update an item in the database (HINT: this function aims to update an object's contents. Think of each grocery item as an entry in a dictionary).
    
## Hosting the App on Heroku (optional)
1. First, go to heroku.com and make an account.
1. Then, while still in the virtual environment, install the Heroku CLI tool following these instructions: https://devcenter.heroku.com/articles/heroku-cli
2. In the terminal, run the following commands:
    ~~~
    heroku login
    heroku create
    ~~~
    These commands will log you into the CLI and create a Heroku project for the current directory.
3. To create a database management system in the Heroku app, run the following command:
    ~~~
    heroku addons:create heroku-postgresql:hobby-dev
    ~~~
    This adds the postgresql RDBMS to our app. You can read more about postgresql [here](https://www.postgresql.org/about/).
4. Next, you'll need to install two libraries so that your app can communicate with the postgressql database.
   ~~~
   pip install psycopg2
   pip install gunicorn
   ~~~
5. Now, you'll need to update the `starter.py` file to communicate with the Heroku database instead of the local `test.db`.
   To do so, add the following import:
   ~~~
   from os import environ
   ~~~
   and change
   ~~~
   app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
   ~~~
   to 
   ~~~
   uri = environ.get('DATABASE_URL')
   if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
   app.config['SQLALCHEMY_DATABASE_URI'] = uri
   ~~~
   This effectively updates the uri to point to the new remote database. The if statement accounts for a Heroku uri inconsistency bug.
6. You now need to create two new files so that Heroku knows how to run your app.
   ~~~
   pip freeze > requirements.txt
   touch Procfile
   ~~~
   `requirements.txt` contains all the required import libraries and `Procfile` states how to run your app.
   Add the following to the `Procfile` file:
   ~~~
   web: gunicorn starter:app
   ~~~
7. Commit and push your changes to Heroku.
   ~~~
   git add .
   git commit -m “initial commit”
   git push heroku main
   ~~~
8. Export your local database to Heroku by doing the following:
   ~~~
   heroku run python
   >>> from app import db
   >>> db.create_all()
   ~~~
   This ensures that Heroku database follows the same table structure as the one saved locally.
9. Now run the Heroku app:
   ~~~
   heroku open
   ~~~
   and you're all set!
   
## Conclusion
Now you're done! That's the basic rundown of how to set up a Flask app using a SQL database through Flask-SQLAlchemy. Even if your team might not be using Flask, take a look as you might be implementing something similar in your project.

For a bonus challenge, suppose we needed to know how much of each item we need on our grocery list. Add an amount column to the `Grocery` object and implement it into your functions.

If you'd like to see the solutions for yourself, switch over to the solution branch and look inside `app.py` for the complete version of `starter.py`.
