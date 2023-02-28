from flask import *
from Capstone.models import db
usr = Blueprint('usr',
                 __name__,
                 template_folder='featUsers/templates',
                 static_folder='featUsers/static',
                 url_prefix='/usr')


# Edit User - Jessica
# usr/edit

# Sign up - Jessica
#usr/signup

# Delete User - Jessica
# usr/del

# view user profile - Jessica
# usr/view

# List and search users - Jamia
# usr/browse

# Reset password - Luke
# usr/reset

# my account page - Jamia
# usr/account

# site notifications - lily