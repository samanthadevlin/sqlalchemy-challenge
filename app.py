import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect 
from flask import Flask, jsonify

#database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect an existing database into a new model 
Base = automap_base()
#reflect tables
Base.prepare(engine, reflect = True)
#save reference to the table 
Measurement = Base.classes.measurement
Station = Base.classes.station

#flask setup
app = Flask(__name__)
#flask routes
@app.route("/")
def welcome():
#"""List all available apt routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start_date><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
#create our session link from python to the DB 
    session = Session(engine)
##"""Return a list of precipitation"""

    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > '2016-08-22').order_by(Measurement.date).all()

   
#create a dictionary from the row data and append to list of date and prcp 
    measure_date = []
    for i in results:
        preci_dict = {}
        preci_dict[i[0]] = i[1]
        #preci_dict = ['prcp'] = precipitation
        measure_date.append(preci_dict)

    return jsonify(measure_date)

@app.route("/api/v1.0/stations")
def stations():
#create our session link from python to the DB 
    session = Session(engine)
#"""Return a list of station"""
    results = session.query(Station.station, Station.name).all()
    session.close()

    return jsonify(results)

@app.route("/api/v1.0/tobs")
def tobs():
#create our session link from python to the DB 
    session = Session(engine)
#"""Return a list of station"""
    results = session.query(Measurement.date, Measurement.tobs, Measurement.station).filter(Measurement.date > '2016-08-22').all()
    session.close()
    tobs_obv = []
    for temperature_observation, date, station in results:
        tobs_temp_dict = {}
        tobs_temp_dict["date"] = date
        tobs_temp_dict["tobs"] = temperature_observation
        tobs_temp_dict["station"] = station
        tobs_obv.append(tobs_temp_dict)
    return jsonify(tobs_obv)

@app.route("/api/v1.0/<start_date>")
def single_date(start_date):
#create our session link from python to the DB 
    session = Session(engine)
#"""Return a list of station""" 
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date >= start_date).all()
    
    single_date = []
    for x in results:
        start_date_dict = {}
        start_date_dict["Min Temp"] = results[0][0]
        start_date_dict["Avg Temp"] = results[0][1]
        start_date_dict["Max Temp"] = results[0][2]
        single_date.append(start_date_dict)

    #session.close()
    return jsonify(single_date)

@app.route("/api/v1.0/<start>/<end>")
def range_date(start, end):
#create our session link from python to the DB 
    session = Session(engine)
#"""Return a list of station""" 
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    range_date = []
    for x in results:
        range_date_dict = {}
        range_date_dict["Min Temp"] = results[0][0]
        range_date_dict["Avg Temp"] = results[0][1]
        range_date_dict["Max Temp"] = results[0][2]
        range_date.append(range_date_dict)

    session.close()
    return jsonify(range_date)

if __name__ == '__main__':
    app.run(debug=True)
