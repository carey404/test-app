import os
import stripe
from flask import Flask, jsonify
from werkzeug.urls import quote as url_quote


app = Flask(__name__)

# Set your Stripe secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = os.getenv('STRIPE_API_KEY')

@app.route('/products')
def get_products():
    try:
        # Fetch all Stripe products
        products = stripe.Product.list()
        
        # Convert Stripe's response to a list of dictionaries simplifying the output
        products_list = [{'id': product['id'], 'name': product['name']} for product in products.auto_paging_iter()]
        
        # Return the list of products as a JSON response
        return jsonify(products_list)
    except stripe.error.StripeError as e:
        # Handle error: e.g., invalid parameters, authentication error
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
