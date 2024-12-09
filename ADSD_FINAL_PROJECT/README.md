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
