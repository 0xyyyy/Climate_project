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

bp_ = Base.classes.bp 

tempOil_ = Base.classes.tempOil

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index.html")
def homepage():
    return render_template('index.html')

@app.route("/view2.html")
def view2():
    return render_template("view2.html")

@app.route("/api/v1.0/tempOil")
def oil():
    session = Session(engine)

    results = session.query(tempOil_.ID, tempOil_.Avg_Temp, tempOil_.Year, tempOil_.Thousand_Barrels_Daily)

    session.close()

    oil_info = []
    for ID, Avg_Temp, Year, Thousand_Barrels_Daily in results:
        oil_dict = {}
        oil_dict["ID"] = ID,
        oil_dict["Avg_Temp"] = Avg_Temp,
        oil_dict["Year"] = Year,
        oil_dict["Thousand_Barrels_Daily"] = Thousand_Barrels_Daily
        oil_info.append(oil_dict)
    return jsonify(oil_info)

@app.route("/api/v1.0/greenhouseGas")
def gas():
    session = Session(engine)

    results = session.query(greenhouseGas_.ID, greenhouseGas_.Country, greenhouseGas_.year, greenhouseGas_.value, greenhouseGas_.category)

    session.close()

    gas_info = []
    for ID, country, year, value, category in results:
        gas_dict = {}
        gas_dict["ID"] = ID,
        gas_dict["Country"] = country,
        gas_dict["year"] = year,
        gas_dict["value"] = value,
        gas_dict["category"] = category
        gas_info.append(gas_dict)
    return jsonify(gas_info)

@app.route("/api/v1.0/bpdata")
def bpData():
    session = Session(engine)

    results = session.query(bp_.ID, bp_.Country, bp_.Year, bp_.pop, bp_.ISO3166_alpha3, bp_.ISO3166_numeric, bp_.Region, bp_.SubRegion, bp_.OPEC, bp_.EU, bp_.OECD, bp_.CIS, bp_.oilcons_ej, bp_.oilcons_kbd, bp_.oilcons_mt, bp_.oilcons_mtoe)

    session.close()

    bp_info = []
    for ID, country, year, pop, ISO3166_alpha3, ISO3166_numeric, region, subregion, opec, eu, oecd, cis, oilcons_ej, oilcons_kbd, oilcons_mt, oilcons_mtoe in results:
        bp_dict = {}
        bp_dict["ID"] = ID,
        bp_dict["country"] = country,
        bp_dict["year"] = year,
        bp_dict["pop"] = pop,
        bp_dict["ISO3166_alpha3"] = ISO3166_alpha3,
        bp_dict["ISO3166_numeric"] = ISO3166_numeric,
        bp_dict["region"] = region,
        bp_dict["subregion"] = subregion,
        bp_dict["OPEC"] = opec,
        bp_dict["EU"] = eu,
        bp_dict["OECD"] = oecd,
        bp_dict["CIS"] = cis,
        bp_dict["oilcons_ej"] = oilcons_ej,
        bp_dict["oilcons_kbd"] = oilcons_kbd,
        bp_dict["oilcons_mt"] = oilcons_mt,
        bp_dict["oilcons_mtoe"] = oilcons_mtoe
        bp_info.append(bp_dict)
    return jsonify(bp_info)

@app.route("/view1.html")
def view1():
    return render_template('view1.html')

    
if __name__ == "__main__":
    app.run(debug=True)