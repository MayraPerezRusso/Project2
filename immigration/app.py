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

<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = "DATA PATH HERE"
db = SQLAlchemy(app)

=======
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/DataFinal.sqlite"
db = SQLAlchemy(app)

# # reflect an existing database into a new model
>>>>>>> 691cb887fda610c672124fc87e9baebe5105b116
Base = automap_base()
# # reflect the tables
Base.prepare(db.engine, reflect=True)

# # Save references to each table
Samples_Metadata = Base.classes.sample_metadata
Samples = Base.classes.samples


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


# @app.route("/names")
# def names():

#     # return jsonify(list(df.columns)[2:])

# @app.route("/metadata/<sample>")
# def sample_metadata(sample):

#     # return jsonify(sample_metadata)

@app.route("/metadata/<sample>/<sample2>")
def sample_metadata(sample, sample2):
    """Return the MetaData for a given sample."""
    if sample is None:
        sample="Total:"
    if sample2 is None:
        sample2=2017
    sel = [
        Samples_Metadata.sample,
        Samples_Metadata.NAME,
        Samples_Metadata.YEAR,
        Samples_Metadata.Latitude,
        Samples_Metadata.Longitude,
    ]

    results = db.session.query(*sel).filter(Samples_Metadata.YEAR == sample2).all()

    # Create a dictionary entry for each row of metadata information!
    sample_metadata = {}
    for result in results:
        sample_metadata["Country"] = result[0]
        sample_metadata["Place"] = result[1]
        sample_metadata["Year"] = result[2]
        sample_metadata["Lat"] = result[3]
        sample_metadata["Lon"] = result[4]
    
    print(sample_metadata)
    return jsonify(sample_metadata)

@app.route("/metadata/<sample>")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    if sample is None:
        sample="Total:"
    sel = [
        Samples_Metadata.sample,
        Samples_Metadata.NAME,
        Samples_Metadata.YEAR,
        Samples_Metadata.Latitude,
        Samples_Metadata.Longitude,
    ]

    results = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information!
    sample_metadata = {}
    for result in results:
        sample_metadata["Country"] = result[0]
        sample_metadata["Place"] = result[1]
        sample_metadata["Year"] = result[2]
        sample_metadata["Lat"] = result[3]
        sample_metadata["Lon"] = result[4]
    
    print(sample_metadata)
    return jsonify(sample_metadata)

# @app.route("/samples/<sample>")
# def samples(sample):

#     # return jsonify(data)


if __name__ == "__main__":
    app.run()
