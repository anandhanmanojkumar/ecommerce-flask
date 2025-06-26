from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
products = [
    {'id': 1, 'name': 'Mobile Phone', 'price': 15000, 'image': 'iphone.jpg'},
    {'id': 2, 'name': 'Laptop', 'price': 60000, 'image': 'macbook.jpg'},
    {'id': 3, 'name': 'Smart Watch', 'price': 5000, 'image': 'watch.jpg'},
    {'id': 4, 'name': 'Shoes', 'price': 2000, 'image': 'shoes.jpg'},
    {'id': 5, 'name': 'Bag', 'price': 1500, 'image': 'bag.jpg'},
    {'id': 6, 'name': 'T-Shirt', 'price': 800, 'image': 'tshirt.jpg'},
    {'id': 7, 'name': 'Shirt', 'price': 1000, 'image': 'shirt.jpg'},
    {'id': 8, 'name': 'Earphones', 'price': 600, 'image': 'earphones.jpg'},
    {'id': 9, 'name': 'Headphones', 'price': 1500, 'image': 'headphones.jpg'}
]


cart = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('product_page'))
    return render_template('home.html')

@app.route('/products')
def product_page():
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/payment_success')
def payment_success():
    cart.clear()
    return render_template('payment_success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
