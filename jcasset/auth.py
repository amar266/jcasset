from flask.ext.httpauth import HTTPBasicAuth
from models import User
import passlib

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return False
    return passlib.hash.md5_crypt.verify(password, user.password_hash)