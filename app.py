from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # This is required for flashing messages

# MongoDB setup
client = pymongo.MongoClient("mongodb+srv://pdevaraj:pdevaraj*01@cluster0.qi00g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['inventory']
products_collection = db['products']

# Password for validation (optional now for add_product route)
PASSWORD = "your_secure_password_here"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operations', methods=['GET', 'POST'])
def operations():
    try:
        # Fetch all products from the database
        products = products_collection.find()
        return render_template('crud.html', products=products)
    except Exception as e:
        flash(f"Error fetching products: {e}", "error")
        return render_template('crud.html', products=[])

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        try:
            # Collect form data
            product_id = request.form['id']
            name = request.form['name']
            stock_level = int(request.form['stock_level'])
            reorder_level = int(request.form['reorder_level'])
            store = request.form['store']
            price = float(request.form['price'])
            password = request.form['password']  # Password to store

            # Check if product with the same product_id already exists
            existing_product = products_collection.find_one({'product_id': product_id})
            if existing_product:
                return render_template('add_product.html', error_message="Product ID already exists!")

            # Insert product into the database along with the password
            products_collection.insert_one({
                'product_id': product_id,
                'name': name,
                'stock_level': stock_level,
                'reorder_level': reorder_level,
                'store': store,
                'price': price,
                'password': password  # Store the password
            })
            flash("Product added successfully!", "success")
            return redirect(url_for('operations'))
        except Exception as e:
            flash(f"Error: {str(e)}", "error")
            return render_template('add_product.html', error_message=f"Error: {str(e)}")

    return render_template('add_product.html')

@app.route('/update_product/<product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    try:
        # Fetch the product details using the ObjectId of the product
        product = products_collection.find_one({'_id': ObjectId(product_id)})
        if not product:
            flash("Product not found!", "error")
            return redirect(url_for('operations'))

        if request.method == 'POST':
            entered_password = request.form['password']
            
            # Ensure the password entered during the update matches the stored password
            if entered_password != product['password']:  # Compare with the stored password
                return render_template('update_product.html', product=product, error_message="Incorrect password!")
            
            # Gather form data to update the product
            updated_data = {
                'product_id': request.form['id'],
                'name': request.form['name'],
                'stock_level': int(request.form['stock_level']),
                'reorder_level': int(request.form['reorder_level']),
                'store': request.form['store'],
                'price': float(request.form['price']),
            }

            # Update product in the database
            products_collection.update_one({'_id': ObjectId(product_id)}, {'$set': updated_data})
            flash("Product updated successfully!", "success")
            return redirect(url_for('operations'))  # Redirect to operations page

        return render_template('update_product.html', product=product)
    except Exception as e:
        flash(f"Error updating product: {e}", "error")
        return redirect(url_for('operations'))

@app.route('/delete_product/<product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    try:
        # Fetch the product details using ObjectId of the product
        product = products_collection.find_one({'_id': ObjectId(product_id)})
        if not product:
            flash("Product not found.", "error")
            return redirect(url_for('operations'))

        if request.method == 'POST':
            entered_password = request.form['password']
            
            # Ensure the password entered matches the stored password
            if entered_password != product['password']:  # Compare with the stored password
                # Pass error message to template if the password is invalid
                return render_template('delete_product.html', product=product, error_message="Invalid password!")

            # Delete the product from the database
            products_collection.delete_one({'_id': ObjectId(product_id)})
            flash(f"Product {product['product_id']} deleted successfully!", "success")
            return redirect(url_for('operations'))  # Redirect to operations page

        return render_template('delete_product.html', product=product)
    except Exception as e:
        flash(f"Error deleting product: {e}", "error")
        return redirect(url_for('operations'))

@app.route('/view_products', methods=['GET'])
def view_products():
    try:
        # Fetch all products from the database
        products = products_collection.find()
        return render_template('view_products.html', products=products)
    except Exception as e:
        flash(f"Error fetching products: {e}", "error")
        return render_template('view_products.html', products=[])

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
