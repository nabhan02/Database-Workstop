from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Grocery %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        grocery = request.form['content']

        new_grocery = Grocery(content=grocery)

        try:
            db.session.add(new_grocery)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding yuour task'
    else:
        groceries = Grocery.query.order_by(Grocery.date_created).all()
        return render_template('index.html', groceries=groceries)


@app.route('/delete/<int:id>')
def delete(id):
    grocery_to_delete = Grocery.query.get_or_404(id)

    try:
        db.session.delete(grocery_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    grocery = Grocery.query.get_or_404(id)

    if request.method == 'POST':
        grocery.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'there was an issue updating your task'
    else:
        return render_template('update.html', grocery=grocery)

if __name__ == "__main__":
    app.run(debug=True)


