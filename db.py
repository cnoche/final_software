from flask import Flask, request, redirect, render_template, jsonify, flash
import math
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:cnoche@localhost/login'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class Message(db.Model):
    message=db.Column(db.String(2000), nullable=False)
    topic=db.Column(db.String(120), primary_key=True, nullable=False) 
    
    def __init__(self, message, topic):
        self.message = message
        self.topic = topic



if __name__ == '__main__':
    db.create_all()

def create_app():
    app = Flask(__name__)
    return app
    
app = create_app()  
