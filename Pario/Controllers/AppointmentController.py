#   FeedbackController.py
#   Description:    Feedback Controller

from Pario import app
from Pario.Models.Appointment import Appointment
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask import abort,request
import time
appointment_collection = Appointment().appointment_collection


def get_appointments(doctor_id):
    if "sort_by" in request.args:
        sortBy = request.args["sort_by"]
    else:
        sortBy = "severity"
    
    if "track" in request.args:
        track = request.args["track"]
    else:
        track = "true"
    #sortBy = "severity"
    data = list(appointment_collection.find({"doctor_id": doctor_id, "track" : track}).sort(sortBy))
    return data
def untrack_appointment(appointmentId):
    appointment = appointment_collection.find_one({"appointment_id": appointmentId})
    if appointment:
        appointment_collection.update_one({"_id" : appointment["_id"]},{"$set" :   {"track" : "false"}})
    return "success"
def epoch(date_time):
    pattern = '%d.%m.%Y %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    return epoch
def message(severity):
    if(severity < -50) :
        return "'s condition has worsened severely"
    if (severity >=-50 and severity <0) :
        return "'s condition has worsened"
    if (severity >=0 and severity <50) :
        return "'s condition has improved"
    if (severity >=50 and severity <80) :
        return " is recovering well"
    if (severity >=80 and severity <100) :
        return " has recovered"

def firstMessage(value):
    if (value> 50):
        return " is recovering"
    else:
        return " is suffering.Please pay attention."

def post_appointment():
    appointmentId = int(request.form['appointment_id'])
    appointment = appointment_collection.find_one({"appointment_id": appointmentId})
    time = request.form["time"]
    patientId = request.form["patient_id"]
    value = request.form["value"]
    doctorId = request.form["doctor_id"]
    name = request.form["name"]
    if appointment:
        feedback = {"feedbacks" : {"time" : time, "value": value}}
        appointment_collection.update(appointment, {'$push' : feedback})
        severity = ((int(value) - int(appointment["feedbacks"][0]["value"])) * 1.0)
        appointment_collection.update_one({"_id" : appointment["_id"]},{"$set" :   {"severity" : severity}})
        appointment_collection.update_one({"_id" : appointment["_id"]},{"$set" :   {"latest" : time}})
        appointment_collection.update_one({"_id" : appointment["_id"]},{"$set" :   {"message" : appointment["name"] + message(severity)}})
    else:
        appointment = {"name": name, "appointment_id" : appointmentId, "doctor_id" : doctorId, "feedbacks" : [{"time" : time, "value": value}], "severity" : 0, "latest" : time, "track" : "true",  "message" : name + firstMessage(int(value))}
        appointment_collection.insert_one(appointment)
    return "success"
