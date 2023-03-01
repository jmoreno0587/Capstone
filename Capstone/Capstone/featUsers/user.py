from flask import *
from Capstone.models import db, Users, Auths
from datetime import datetime
usr = Blueprint('usr',
                 __name__,
                 template_folder='featUsers/templates',
                 static_folder='featUsers/static',
                 url_prefix='/usr')

# use render_template('file.html',title = 'mod name', year = datetime.now().year))

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
@usr.route('/browse')
def browse_Users():
    users = Users.query.all()
    res = {}
    for user in users:
        res[user.userID] = {
        'userName': user.userName,
        'email': user.email
        }
    return jsonify(res)

@usr.route('/auth')
def view_Auths():
    auths = Auths.query.all()
    res = {}
    for auth in auths:
        res[auth.authID] = {
        'username': auth.username,
        'hashpassword': auth.hashpassword
        }
    return jsonify(res)

# Reset password - Luke
# usr/reset

# my account page - Jamia
# usr/account

# site notifications - lily