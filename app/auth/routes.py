from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from models import User, db

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer', realm=None, header=None)

@basic_auth.verify_password
def verify(email, password):
    user = db.session.execute(db.select(User).where(User.email==email)).scalar()
    if user is not None and user.check_password(password):
        return user
    return None

@basic_auth.error_handler
def handle_error(status):
    return {'error': 'Incorrect email and/or password'}, status

@token_auth.verify_token
def verify_token(token):
    return User.query.filter_by(token=token).first()