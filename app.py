import numpy as no
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, func, inspect 
from flask import Flask, jsonify

#database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect an existing database into a new model 
Base = automap_base()
#reflect tables
Base.prepare(engine, refect = True)
#save reference to the table 
Measurement = Base.classes.measurement
Station = Base.classes.station

#flask setup
app = Flask(__name__)
#flask routes
@app.route("/")
def welcome()
"""List all available apt routes."""
return(
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation"
    f"/api/v1.0/stations"
    f"/api/v1.0/tobs"
)

@app.route("/api/v1.0/precipitation")
def precipitation()
#create our session link from python to the DB 
session = Session(engine)
"""Return a list of precipitation"""
results = session.query(Measurement.date, Measurement.prcp).all()
session.close()
#create a dictionary from the row data and append to list of date and prcp 
measure_date = []
for date, prcp in results:
    preci_dict = {}
    preci_dict = ["date"] = date
    preci_dict = ['prcp'] = precipitation
    measure_date.append(preci_dict)
return jsonify(measure_date)

@app.route("/api/v1.0/stations")
def stations()
#create our session link from python to the DB 
session = Session(engine)
"""Return a list of station"""
results = session.query(Station.station, Station.name).all()
session.close()

@app.route("/api/v1.0/tobs")
def tobs()
#create our session link from python to the DB 
session = Session(engine)
"""Return a list of station"""
results = session.query(Measurement.date, Measurement.tobs, Measurement.station).filter(Measurement.date > '2016-08-22').all()
session.close()
tobs_obv = []
for temperature observation, date, station in results:
    tobs_temp_dict = {}
    tobs_temp_dict["date"] = date
    tobs_temp_dict["tobs"] = temperature_observation
    tobs_temp_dict["station"] = station
tobs_obv.append(tobs_temp_dict)
return jsonify(tobs_obv)

@app.route("/api/v1.0/<start>")
def start_date()
#create our session link from python to the DB 
session = Session(engine)
"""Return a list of station""" 
results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs).all()
session.close()
return jsonify(start_date)

@app.route("/api/v1.0/<start>/<end>")
def end_date()
#create our session link from python to the DB 
session = Session(engine)
"""Return a list of station""" 
results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs).all()
session.close()
return jsonify(end_date)

if __name__ == '__main__'
app.run(debug=True)
