from flask import Flask



app= Flask(__name__, template_folder='views')
app.secret_key ='OdsaASE432FDdfdaaQqqerA3sVEb2PLu1p'
from src.controllers import *



def create_app():
    app.run(debug = True)

