#   router.py
#   Description:    ...

import json
from flask import Flask, Response, request
from Pario import app
from Pario.Controllers import AppointmentController
from bson.json_util import dumps
#   Index page
@app.route(
     '/',
     methods=['GET']
)
def get_index():
    return Response('Welcome to Aurora!')

@app.route(
     '/get/appointments/<doctor_id>',
     methods=['GET']
)
def get_appointments(doctor_id):
    return Response(
            dumps(
                {
                    'response' : AppointmentController.get_appointments(doctor_id)
                }
            ),
            mimetype='application/json',
            status=200
    )


@app.route(
     '/appointments',
     methods=['POST']
)
def post_appointment():
    return Response(
            dumps(
                {
                    'response' : AppointmentController.post_appointment()
                }
            ),
            mimetype='application/json',
            status=200
    )
