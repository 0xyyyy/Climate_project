# import dependencies 
from flask import Flask, jsonify, render_template
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

engine = create_engine("sqlite:///db.sqlite")

#check that engine connection is working 
# print(pd.read_sql("SELECT * FROM greenhouseGas", engine))

Base = automap_base()

Base.prepare(engine, reflect=True)

greenhouseGas_ = Base.classes.greenhouseGas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
        f"Available Routes:<br>"
        f"/api/v1.0/greenhouseGas<br>"
        f"/api/v1.0/bpdata<br>"

@app.route("/view1.html")
def view1():
    return render_template('view1.html')

    
