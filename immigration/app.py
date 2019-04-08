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
app.config["SQLALCHEMY_DATABASE_URI"] = "TestSQLdb.sqlite"
db = SQLAlchemy(app)
=======
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/TestSQLdb.sqlite"
# db = SQLAlchemy(app)
>>>>>>> 467d070d3a0e1aab069fc6b8e39873392f13680c

# Base = automap_base()
# # # reflect the tables
# Base.prepare(db.engine, reflect=True)

<<<<<<< HEAD
# # Save references to each table
Samples_Metadata = Base.classes.immigration

=======
# # # Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples
data=pd.read_csv('db/DataFinaltosqlite.csv')
>>>>>>> 467d070d3a0e1aab069fc6b8e39873392f13680c


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
<<<<<<< HEAD
    stmt = db.session.query(Samples_Metadata).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    # Return a list of the column names (sample names)
    return jsonify(df["NAME"].tolist())



# @app.route("/metadata/<sample>")
# def sample_metadata(sample):

#     # return jsonify(sample_metadata)

# @app.route("/metadata/<sample>/<sample2>")
# def sample_metadata(sample, sample2):
#     """Return the MetaData for a given sample."""
#     if sample is None:
#         sample="Total:"
#     if sample2 is None:
#         sample2=2017
#     sel = [
#         Samples_Metadata.sample,
#         Samples_Metadata.NAME,
#         Samples_Metadata.YEAR,
#         Samples_Metadata.Latitude,
#         Samples_Metadata.Longitude,
#     ]

#     results = db.session.query(*sel).filter(Samples_Metadata.YEAR == sample2).all()

#     # Create a dictionary entry for each row of metadata information!
#     sample_metadata = {}
#     for result in results:
#         sample_metadata["Country"] = result[0]
#         sample_metadata["Place"] = result[1]
#         sample_metadata["Year"] = result[2]
#         sample_metadata["Lat"] = result[3]
#         sample_metadata["Lon"] = result[4]
    
#     print(sample_metadata)
#     return jsonify(sample_metadata)

# @app.route("/metadata/<sample>")
# def sample_metadata(sample):
#     """Return the MetaData for a given sample."""
#     if sample is None:
#         sample="Total:"
#     sel = [
#         Samples_Metadata.sample,
#         Samples_Metadata.NAME,
#         Samples_Metadata.YEAR,
#         Samples_Metadata.Latitude,
#         Samples_Metadata.Longitude,
      
#     ]

#     results = db.session.query(*sel).all()
    
#     # Create a dictionary entry for each row of metadata information!
#     sample_metadata = {}
#     for result in results:
#         sample_metadata["Country"] = result[0]
#         sample_metadata["Place"] = result[1]
#         sample_metadata["Year"] = result[2]
#         sample_metadata["Lat"] = result[3]
#         sample_metadata["Lon"] = result[4]
       
    
#     print(sample_metadata)
#     return jsonify(sample_metadata)

# app.route("/metadata/Histogram")
# def sample_metadata(sample):
#     """Return the MetaData for a given sample."""
#     if sample is None:
#         sample="Total:"
#     sel = [
#         Samples_Metadata.sample,
#         Samples_Metadata.NAME,
#         Samples_Metadata.YEAR,
#         Samples_Metadata.Latitude,
#         Samples_Metadata.Longitude,
#         Samples_Metadata.Total:,
#     ]

#     results = db.session.query(*sel).all()
#     df = pd.read_sql_query(results, db.session.bind)
#     final_df = df.sort_values(by=[‘Total:’], ascending=False).nlargest(10, ‘Total:’)


#     # Format the data to send as json
#     sample_metadata = {
#                   "Country": final_df.Sample.values.tolist(),
#                   "Place": final_df.Name.values.tolist(),
#                   "Year": final_df.Year.tolist(),
# 		          "Lat": final_df.Lat.tolist(),
# 		          "Lon": final_df.Lon.tolist(),
# 		          "Total": final_df.Total:.tolist(),
#     }
#     print(sample_metadata)

#     return jsonify(sample_metadata)
=======
    # stmt = db.session.query(Samples).statement
    # df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(list(data.columns.values)[8:])   

@app.route("/metadata/<sample>/<sample2>/")
def sample_metadata(sample, sample2):
    if sample is None:
        sample="Total"
    if sample2 is None:
        sample2=2017
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
>>>>>>> 467d070d3a0e1aab069fc6b8e39873392f13680c

    return jsonify(sample_metadata2)



if __name__ == "__main__":
    app.run()
