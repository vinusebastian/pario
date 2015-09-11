#   __init__.py
#   Description:    ...

from flask import Flask

app = Flask('Pario')
app.config.from_object('Pario.configs')

import router

