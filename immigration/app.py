import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# #################################################
# # Database Setup
# #################################################

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/TestSQLdb.sqlite"
# db = SQLAlchemy(app)

# Base = automap_base()
# # # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # # Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples
data=pd.read_csv("~/immigration/db/dataFile.csv")


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    # stmt = db.session.query(Samples).statement
    # df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(list(data.columns.values)[8:])   

@app.route("/metadata/<sample>/<sample2>/")
def sample_metadata(sample, sample2):
    # if sample is "undefined":
    #     sample="Total"
    # if sample2 is "undefined":
    #     sample2=2017
    data1=data[data['Year'] == int(sample2)]
    data1=data1[[sample, "NAME", "Year", "latitude", "longitude"]]
    data1['country']=data1[sample]
    data1=data1.sort_values(by=[sample], ascending=False)
    sample_metadata = data1.to_dict('list')

    # print(type(int(sample2)))

    return jsonify(sample_metadata)

@app.route("/metadata/<sample>/")
def sample_metadata2(sample):
    
    data1=data[[sample, "NAME", "Year", "latitude", "longitude"]]
    data2=data1.groupby(['Year']).sum()
    data2['country']=data2[sample]
    data2['Year']=[2014,2015,2016,2017]
    
    sample_metadata2 = data2.to_dict('list')

    # print(type(int(sample2)))

    return jsonify(sample_metadata2)



if __name__ == "__main__":
    app.run()
