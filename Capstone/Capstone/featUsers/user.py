from flask import *

usr = Blueprint('usr',
                 __name__,
                 template_folder='templates',
                 static_folder='static',
                 url_prefix='/usr')


# Edit User - Jessica
# usr/edit
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