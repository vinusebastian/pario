#   Person.py
#   Description:    ...

from Pario import app
import pymongo
import json
from Base import Base


class Appointment(Base):

    def __init__(self):
        Base.__init__(self)
        self.appointment_collection = self.db.appointments
