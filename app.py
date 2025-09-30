
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Hardcoded product list
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 50000, "imageUrl": "/static/images/laptop.jpg"},
    {"id": 2, "name": "Headphones", "price": 2000, "imageUrl": "/static/images/headphones.jpg"},
    {"id": 3, "name": "Smartphone", "price": 25000, "imageUrl": "/static/images/phone.jpg"},
    {"id": 4, "name": "Keyboard", "price": 1500, "imageUrl": "/static/images/keyboard.jpg"},
    {"id": 5, "name": "Mouse", "price": 800, "imageUrl": "/static/images/mouse.jpg"},
    {"id": 6, "name": "Tablet", "price": 18000, "imageUrl": "/static/images/tablet.jpg"},
    {"id": 7, "name": "Smartwatch", "price": 7000, "imageUrl": "/static/images/smartwatch.jpg"},
    {"id": 8, "name": "Camera", "price": 30000, "imageUrl": "/static/images/camera.jpg"},
    {"id": 9, "name": "Speaker", "price": 3500, "imageUrl": "/static/images/speaker.jpg"},
    {"id": 10, "name": "Monitor", "price": 60000, "imageUrl": "/static/images/monitor.jpg"},
    {"id": 11, "name": "Printer", "price": 40000, "imageUrl": "/static/images/printer.jpg"},
    {"id": 12, "name": "Appliances", "price": 70000, "imageUrl": "/static/images/appliances.jpg"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(PRODUCTS)

@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.json
    print("Received order:", data)  # Logs order in console
    return jsonify({"message": "Order placed successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
