from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import environ

app = Flask(__name__)
uri = environ.get('DATABASE_URL')
if uri and uri.startswith("postgres://"):
     uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
db = SQLAlchemy(app)

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #bonus challenge: add an amount column

    def __repr__(self):
        return '<Grocery %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #implement the post request
        #you need to capture the input from the form and make a grocery object
        #add the grocery to the update similar to staging a git commit
        # you then need to commit that change to the database
        #you then have to redirect to the database
        pass
    else:
        # the get request
        groceries = Grocery.query.order_by(Grocery.date_created).all()
        return render_template('index.html', groceries=groceries)


@app.route('/delete/<int:id>')
def delete(id):
    #implement the delete function
    #get the element from the dataase, delete from database, commit change, redirect to index.html
    pass

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    #implement update
    #Use skills from previous methods to solve this method ***HINT: DATABASE ARE A LOT LIKE DICTIONARIES***
    pass

if __name__ == "__main__":
    app.run(debug=True)


