from flask import *
from Capstone.models import db
proj = Blueprint('proj',
                 __name__,
                 template_folder='templates',
                 static_folder='static',
                 url_prefix='/proj')

# create project - Jamia
# proj/new

# edit/ delete project - Jessica
# proj/edit
# proj/del

# Find and search projects - Jamia
# proj/browse

# project view based on role - luke
# proj/view

# appy/accept to project - Luke

# invite to project - Lily

# project calendar - luke