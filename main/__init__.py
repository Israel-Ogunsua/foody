from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__) 
app.config["SECRET_KEY"] ='9ab622881a119dadd6df2ca5'

from main import route