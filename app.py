# import dependencies for python
import datetime as dt
import numpy as np
import pandas as pd
# sql dependencies
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 
# flask dependencies
from flask import Flask, jsonify

# create engine
engine = create_engine("sqlite:///hawaii.sqlite")
# set up base and classes
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create session
session = Session(engine)

# Set up Flask app
app = Flask(__name__)
@app.route("/")
def welcome():
    return(
    '''

    Welcome to the Climate Analysis API!\n
    Available Routes:\n
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/temp/start/end\n
    '''
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def station():
    results = session.query(Station.sattion).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Left off on 9.5.5