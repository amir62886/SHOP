from flask import Flask, render_template

app = Flask(__name__)

class Product():
    def __init__(self, id, name, price, description, imageName = "i.webp"):
        self.Id = id
        self.name = name
        self.price = price
        self.description = description
        self.imageName = imageName

products = []
products.append(Product(1, "Apple", 11000, "delicious", "apple.webp"))
products.append(Product(2, "Orange", 40000, "more delicious", "orange.webp"))
products.append(Product(3, "Lemon", 25000, "sour", "lemon.webp"))        

@app.route("/")
def home():
    return render_template("homePage.html", products = products)

@app.route("/product/<int:id>")
def product(id):
    return render_template("product.html", product = products[id - 1])

@app.route("/about")
def about():
    return "О нас"