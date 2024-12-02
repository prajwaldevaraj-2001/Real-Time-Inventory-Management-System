from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import math

app = Flask(__name__)

# MongoDB connection string
MONGO_URI = "mongodb+srv://pdevaraj:pdevaraj*01@cluster0.qi00g.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["inventory"]
product_collection = db["products"]

# Pagination configuration
ITEMS_PER_PAGE = 5

@app.route('/')
def home():
    return redirect(url_for('view_products', page=1))

@app.route('/products')
def view_products():
    page = int(request.args.get('page', 1))
    total_products = product_collection.count_documents({})
    total_pages = math.ceil(total_products / ITEMS_PER_PAGE)
    products = list(
        product_collection.find()
        .skip((page - 1) * ITEMS_PER_PAGE)
        .limit(ITEMS_PER_PAGE)
    )
    return render_template(
        'view_products.html',
        products=products,
        current_page=page,
        total_pages=total_pages
    )

@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        product_data = {
            "name": request.form['name'],
            "description": request.form['description'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        product_collection.insert_one(product_data)
        return redirect(url_for('view_products', page=1))
    return render_template('create_product.html')

@app.route('/update_product/<product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    from bson.objectid import ObjectId
    product = product_collection.find_one({"_id": ObjectId(product_id)})
    if request.method == 'POST':
        updated_data = {
            "name": request.form['name'],
            "description": request.form['description'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        product_collection.update_one({"_id": ObjectId(product_id)}, {"$set": updated_data})
        return redirect(url_for('view_products', page=1))
    return render_template('update_product.html', product=product)

@app.route('/delete_product/<product_id>', methods=['POST'])
def delete_product(product_id):
    from bson.objectid import ObjectId
    product_collection.delete_one({"_id": ObjectId(product_id)})
    return redirect(url_for('view_products', page=1))

if __name__ == '__main__':
    app.run(debug=True)
