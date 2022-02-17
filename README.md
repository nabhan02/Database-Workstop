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
    
## Hosting the App on Heroku
## Conclusion
Now you're done! That's the basic rundown of how to set up a Flask app using a SQL database through Flask-SQLAlchemy. Even if your team might not be using Flask, take a look as you might be implementing something similar in your project.

For a bonus challenge, suppose we needed to know how much of each item we need on our grocery list. Add an amount column to the `Grocery` object and implement it into your functions.

If you'd like to see the solutions for yourself, switch over to the solution branch and look inside `app.py` for the complete version of `starter.py`.
