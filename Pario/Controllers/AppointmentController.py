#   FeedbackController.py
#   Description:    Feedback Controller

from Pario import app
from Pario.Models.Appointment import Appointment
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask import abort,request

appointment_collection = Appointment().appointment_collection


def get_appointments(doctor_id):
    data = list(appointment_collection.find({"doctor_id": doctor_id}))
    if len(data) == 0:
        abort(404)
    return data

def post_appointment():
    appointmentId = int(request.args['appointment_id'])
    appointment = appointment_collection.find_one({"appointment_id": appointmentId})
    time = request.args["time"]
    patientId = request.args["patient_id"]
    value = request.args["value"]
    doctorId = request.args["doctor_id"]
    if appointment:
        feedback = {"feedbacks" : {"time" : time, "value": value}}
        appointment_collection.update(appointment, {'$push' : feedback})
    else:
        appointment = {"appointment_id" : appointmentId, "doctor_id" : doctorId, "feedbacks" : [{"time" : time, "value": value}], "delta" : 0}
        appointment_collection.insert_one(appointment)
    return "success"
