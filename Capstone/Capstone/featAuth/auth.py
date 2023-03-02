from flask import *
from Capstone.models import db, Users
from datetime import datetime
auth = Blueprint('auth',
                 __name__,
                 template_folder='templates',
                 static_folder='static',
                 url_prefix='/auth')

# Login in log out, user session - lily


### define read and write permissions to our server
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    #regex = re.compile(r'(^[A-Z0-9_!#$%&'*+/=?`{|}~^.-]+@[A-Z0-9.-]+$)')
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        print(f"the username: {username} was sent in a POST req")
        pw1 = request.form.get("pw1")
        pw2 = request.form.get("pw2")
        email_exists = Users.query.filter_by(email=email).first()
        username_exists = Users.query.filter_by(userName=username).first()
        if email_exists:
            flash('Email is already taken.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif pw1 != pw2:
            flash('Passwords do not match', category='error')
        elif len(username) < 2:
            flash('Username is too short',category='error')
        elif len(pw1) < 8:
            flash('Password is too short',category='error')
        ##email regex to escape SQL injection ^[A-Z0-9_!#$%&'*+/=?`{|}~^.-]+@[A-Z0-9.-]+$
        ## https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address
        # elif not re.match(regex,email):
        #     flash('Invalid email', category='error')
        else:
            #new_user = User(email=email,username=username,
            #                password=generate_password_hash(pw1, method='sha256'))
            #db.session.add(new_user)
            #db.session.commit()
            #login_user(new_user, remember=True)
            flash('User account created!',category='success')
            return redirect(url_for('home'))
    return render_template("SignUp.html", title = 'Sign Up', year = datetime.now().year)