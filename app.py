import os
from flask import Flask
from models import setup_db
from flask_cors import CORS

def dymko_fun():
    return "This page is created by dymko!!!"

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': 
            greeting = greeting + "!!!!! You are doing great in this Udacity project."
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"
    
    @app.route('/dymko')
    def be_dymko():
        text = dymko_fun()
        return text

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
