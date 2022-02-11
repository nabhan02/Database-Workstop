# Database-Workstop

Today we'll go over how to set up a database using Flask-SQLAlchemy and connect it to a simple mobile app. Before we begin, clone this repository into a local directory that you want to use for this project. Also, make sure you have the latest versions of Python and virtualenv installed. If you haven't downloaded them yet, you can visit this link for Python: https://www.python.org/downloads/ and follow the instructions below for virtualenv.

## Installing Virtualenv

Run this command in your terminal to install virtualenv:
    
    pip install virtualenv

## Installing Flask and Flask-SQLAlchemy

1. Open your terminal and create a virtual environment:

    For macOS/Linux:
    ~~~
    $ python3 -m venv venv
    ~~~
    For Windows:
    ~~~
    > py -m venv venv
    ~~~
2. Then, activate your virtual environment

    For macOS/Linux:
    ~~~
    $ . venv/bin/activate
    ~~~
    For Windows:
    ~~~
    > venv\Scripts\activate
    ~~~
3. Finally, run the following lines to install Flask and Flask-SQLAlchemy using pip:
    ~~~
    $ pip install Flask
    $ pip install -U Flask-SQLAlchemy
    ~~~

## Creating a Basic Database

1. Take a look at the two files in your directory, `app.py` and `index.html`. `app.py` contains a basic Flask application that displays the content from `index.html`. 
2. Let's take a look at our rudimentary webapp. From your project directory, run the following command and go to `localhost:5000` to take a look:
    For macOS/Linux:
    ~~~
    $ python3 app.py
    ~~~
    For Windows:
    ~~~
    > py app.py
    ~~~
3. Now let's add a database to our webapp to store and retrieve information. Add the following code into `app.py`.
    ~~~
    insert code
    ~~~
    This code will...
5. Update index.html.
6. Add the following code into `app.py`.
    ~~~
    insert code
    ~~~
    This code will...
7. Update index.html.
