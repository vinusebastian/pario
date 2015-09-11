#   router.py
#   Description:    ...

import json
from flask import Flask, Response
from Pario import app


#   Index page
@app.route(
     '/',
     methods=['GET']
)
def get_index():
    return Response('Welcome to Aurora!')
