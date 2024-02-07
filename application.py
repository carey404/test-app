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
        product = stripe.Product.retrieve('prod_PW4OvOwEwn3TnW')

        # Use render_template to serve your HTML page with the pretty printed JSON
        return render_template('index.html', data=product)
    except stripe.error.StripeError as e:
        # Handle error by rendering the error message in the template within `pre` tags
        error_message = json.dumps({'error': str(e)}, indent=4)
        return render_template('index.html', data=error_message), 400

if __name__ == '__main__':
    application.run(debug=True)
