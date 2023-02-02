"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Capstone.views
from Capstone.featAuth.auth import auth
app.register_blueprint(auth)

from Capstone.featUsers.user import usr
app.register_blueprint(usr)

from Capstone.featProjects.projects import proj
app.register_blueprint(proj)