# Real-Time Inventory Management System

This project is a Real-Time Inventory Management System developed using MongoDB, Flask, and WebSocket. The system tracks inventory levels and updates in real-time, enabling businesses to manage stock efficiently and prevent overstocking or stockouts.

## Project Structure

```plaintext
Real-Time-Inventory-Management-System/
│
├── app.py                      # Main Flask application file
├── templates/                  # HTML templates used in the web interface
│   ├── index.html              # Home page (dashboard)
│   ├── add_product.html        # Form to add new products
│   ├── update_product.html     # Form to update product details
│   ├── delete_product.html     # Confirmation page for deleting products
│   ├── view_products.html      # Displays a list of all products
│   └── crud.html               # CRUD operations page
│
├── static/                     # Static files (CSS, JS, Images)
│   └── css/
│       └── styles.css          # Styles for the system
│
├── README.md                   # Project description and structure
└── requirements.txt            # Python dependencies


Features
User Authentication: Password-based validation for updating and deleting products.
CRUD Operations:
Create: Add new products to the inventory.
Read: View the list of all products stored in the inventory.
Update: Modify product details, such as stock level, price, and reorder level.
Delete: Remove products from the inventory.
Interactive Maps: Links to maps for various product purchase locations (e.g., Walmart, Acme Fresh Market).
Team Members Section: View roles and tasks of the team working on the project.
Technologies Used
Backend: Flask (Python)
Database: MongoDB
Frontend: HTML, CSS, JavaScript
WebSocket: Real-time data interaction for inventory management
Interactive Maps: Integration of clickable map links for store locations.
Installation
To run this project locally, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/prajwaldevaraj-2001/project.git
Install dependencies:

Navigate to the project directory and install the required packages.
bash
Copy
Edit
pip install -r requirements.txt
Set up MongoDB:

Ensure that you have MongoDB installed locally or use a cloud-based MongoDB service (like MongoDB Atlas).
Update the MongoDB connection details in the app.py file, if needed.
Run the application:

Start the Flask server.
bash
Copy
Edit
python app.py
Open the application:

Go to http://localhost:5000 in your web browser to start using the Real-Time Inventory Management System.
How It Works
Dashboard
Action Buttons: Navigate to pages for adding, viewing, and managing products.
Interactive Maps: Links to maps for stores like Walmart and Acme Fresh Market.
Team Members Section: Introduces the project team and displays their roles and tasks.
CRUD Operations
Create (Add Product):

Navigate to the Add Product page and fill out the product form.
If a product already exists, an error message will appear.
View Products:

A table dynamically displays product details from the MongoDB database.
Update:

Edit product details such as stock level and price. Password validation is required.
Delete:

Confirm deletion of products using password validation.
MongoDB Database
Storing Data: Products are stored as documents in MongoDB with fields such as Product ID, Name, Stock Level, Reorder Level, Store, and Price.
Displaying Data: The product information is queried from MongoDB and displayed on the view_product.html page dynamically.
Team Members
Prajwal Devaraj: Backend Development (MongoDB, Flask)
Sai Supriya Lokam: Frontend Development (HTML, CSS, JavaScript)
Khyathi Swaroop Pathangay: Real-Time Data Interaction (WebSocket)
Future Improvements
Implement automated email or SMS notifications for low stock alerts.
Integrate advanced data analytics to predict inventory needs based on historical data.
Add a user authentication system for restricted access to product management operations.
