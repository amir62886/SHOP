from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
app.app_context().push()
db = SQLAlchemy (app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float)   
    description = db.Column(db.String)   
    imageName = db.Column(db.String) 
      
@app.route("/")   
def home():
    return render_template("homePage.html", products = products)

@app.route("/product/<int:id>")
def product(id):
    return render_template("product.html", product = products[id - 1])

@app.route("/about")
def about():
    return "О нас"