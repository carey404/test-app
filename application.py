import os
import stripe
import json
from flask import Flask, jsonify, render_template
from werkzeug.urls import quote as url_quote


application = Flask(__name__)

application.static_folder = 'static'

stripe.api_key = os.getenv('STRIPE_API_KEY')

@application.route('/')
def get_products():
    try:
        # Fetch all Stripe products
        products = stripe.Product.list()
        
        # Convert Stripe's response to a list of dictionaries simplifying the output
        products_list = [{'id': product['id'], 'name': product['name']} for product in products.auto_paging_iter()]
        
        # Pretty print the JSON data with an indent of 4 spaces
        pretty_products = json.dumps(products_list, indent=4)


        # Use render_template to serve your HTML page with the pretty printed JSON
        return render_template('index.html', data=products_list)
    except stripe.error.StripeError as e:
        # Handle error: e.g., invalid parameters, authentication error
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    application.run(debug=True)
