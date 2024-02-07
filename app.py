from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    secret_api_key = os.environ.get('SECRET_API_KEY', 'Default API Key')
    # In a real scenario, you would use the secret API key to fetch data from an API.
    return f'Hello, your secret API key is: {secret_api_key}'

if __name__ == '__main__':
    app.run()
