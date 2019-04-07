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

app.config["SQLALCHEMY_DATABASE_URI"] = "DATA PATH HERE"
db = SQLAlchemy(app)

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


# @app.route("/samples/<sample>")
# def samples(sample):

#     # return jsonify(data)


if __name__ == "__main__":
    app.run()
