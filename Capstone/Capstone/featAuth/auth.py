from flask import *
from Capstone.models import db
auth = Blueprint('auth',
                 __name__,
                 template_folder='templates',
                 static_folder='static',
                 url_prefix='/auth')

# Login in log out, user session - lily