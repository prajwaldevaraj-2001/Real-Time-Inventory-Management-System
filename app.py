from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection configuration
app.config["MONGO_URI"] = "mongodb+srv://pdevaraj:pdevaraj*01@cluster0.qi00g.mongodb.net/mydatabase?retryWrites=true&w=majority"  # Update with your own credentials
mongo = PyMongo(app)

# Define collection
product_collection = mongo.db.products

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def view_products():
    # Pagination
    page = int(request.args.get('page', 1))
    products_per_page = 10
    products = product_collection.find().skip((page - 1) * products_per_page).limit(products_per_page)
    total_products = product_collection.count_documents({})
    total_pages = (total_products // products_per_page) + (1 if total_products % products_per_page > 0 else 0)
    return render_template('view_products.html', products=products, page=page, total_pages=total_pages)

@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        description = request.form['description']
        
        # Insert product into database
        product_collection.insert_one({
            'name': name,
            'price': price,
            'stock': stock,
            'description': description
        })
        
        return redirect(url_for('view_products'))
    
    return render_template('create_product.html')

@app.route('/update_product/<product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = product_collection.find_one({'_id': ObjectId(product_id)})
    
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        description = request.form['description']
        
        # Update product in database
        product_collection.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': {
                'name': name,
                'price': price,
                'stock': stock,
                'description': description
            }}
        )
        
        return redirect(url_for('view_products'))
    
    return render_template('update_product.html', product=product)

@app.route('/delete_product/<product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    # Delete product from database
    product_collection.delete_one({'_id': ObjectId(product_id)})
    return redirect(url_for('view_products'))

if __name__ == '__main__':
    app.run(debug=True)
