# imports 
from flask_sqlalchemy import SQLAlchemy
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# New Models
#######################################################################################
class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    token = db.Column(db.String, default = '', unique = True )
    isAdmin = db.Column(db.Boolean, default = False)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    phone_number = db.Column(db.String(20), nullable = False)
    address_street = db.Column(db.String(100), nullable = False)
    address_city = db.Column(db.String(50), nullable = True)
    address_state = db.Column(db.String(2), nullable = True)
    address_zipcode = db.Column(db.String(9), nullable = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    cart = db.relationship('Usercart', backref='user', lazy=True)
    cc = db.relationship('Usercc', backref='user', lazy=True)
    payment = db.relationship('Userpayment', backref='user', lazy=True)

    def __init__(self, isAdmin, first_name, last_name, email, password, phone_number, address_street, address_city, address_state, address_zipcode):
        self.id = self.set_id()
        self.token = self.set_token(24)
        self.isAdmin = isAdmin
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.phone_number = phone_number
        self.address_street = address_street
        self.address_city = address_city
        self.address_state = address_state
        self.address_zipcode = address_zipcode

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_token(self):
        return self.token
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'token', 'isAdmin', 'first_name', 'last_name', 'password', 'email', 'phone_number', 'address_street', 'address_city', 'address_state', 'address_zipcode', 'date_created']

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Bikeconfig(db.Model):
    id = db.Column(db.String, primary_key = True)
    make = db.Column(db.String(20), nullable = False, default = 'Specialized')
    model = db.Column(db.String(20), nullable = False)
    year = db.Column(db.String(5), nullable = False, default = '2024')
    color = db.Column(db.String(30), nullable = False)
    trim = db.Column(db.String(30), nullable = True, default = '')
    category = db.Column(db.String(30), nullable = True, default = '')
    size = db.Column(db.Integer, nullable = False)
    cost = db.Column(db.Numeric(precision=6, scale=2), nullable = False)
    carted = db.relationship('Usercart', backref='bikeconfig', lazy=True)

    def __init__(self, make, model, year, color, category, trim, size, cost):
        self.id = self.set_id()
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.category = category
        self.trim = trim
        self.size = size
        self.cost = cost

    def set_id(self):
        return str(uuid.uuid4())
    
class BikeConfigSchema(ma.Schema):
    class Meta:
        fields = ['id', 'make', 'model', 'year', 'color', 'trim', 'category', 'size', 'cost']

bike_config_schema = BikeConfigSchema()
bikes_config_schema = BikeConfigSchema(many=True)

class Usercart(db.Model):
    id = db.Column(db.String, primary_key = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    bike_id = db.Column(db.String, db.ForeignKey('bikeconfig.id'), nullable = False)
    quantity = db.Column(db.Integer, nullable = True, default = 1)
    itemtotal = db.Column(db.Numeric(10,2), nullable = True)
      
    def __init__(self, user_token, bike_id, quantity, itemtotal ):
        self.id = self.set_id()
        self.user_token = user_token
        self.bike_id = bike_id
        self.quantity = quantity
        self.itemtotal = itemtotal
        
    def set_id(self):
        return str(uuid.uuid4())

class UsercartShema(ma.Schema):
    class Meta:
        fields = ['id', 'user_token', 'bike_id', 'quantity', 'itemtotal']

usercart_schema = UsercartShema()
usercarts_schema = UsercartShema(many=True)

class Usercc(db.Model):
    id = db.Column(db.String, primary_key = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    cc_num = db.Column(db.String(20), nullable = False, unique = True)
    cc_date = db.Column(db.String(10), nullable = False)
    cc_code = db.Column(db.String(5), nullable = False)
    cc_zip = db.Column(db.String(9), nullable = False)
      
    def __init__(self, user_token, cc_num, cc_date, cc_code, cc_zip):
        self.id = self.set_id()
        self.user_token = user_token
        self.cc_num = cc_num
        self.cc_date = cc_date
        self.cc_code = cc_code
        self.cc_zip = cc_zip
        
    def set_id(self):
        return str(uuid.uuid4())

class UserccShema(ma.Schema):
    class Meta:
        fields = ['id', 'user_token', 'cc_num', 'cc_date', 'cc_code', 'cc_zip']

usercc_schema = UserccShema()
userccs_schema = UserccShema(many=True)


class Userpayment(db.Model):
    id = db.Column(db.String, primary_key = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    items = db.Column(db.PickleType, nullable=False)
    delivery_details = db.Column(db.PickleType, nullable=False)
    subtotal = db.Column(db.Numeric(10,2), nullable = False)
    tax = db.Column(db.Numeric(10,2), nullable = False)
    total = db.Column(db.Numeric(10,2), nullable = False)
    date_placed = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
      
    def __init__(self, user_token, items, delivery_details, subtotal, tax, total):
        self.id = self.set_id()
        self.user_token = user_token
        self.items = items
        self.delivery_details = delivery_details
        self.subtotal = subtotal
        self.tax = tax
        self.total = total
        
    def set_id(self):
        return str(uuid.uuid4())

class UserpaymentShema(ma.Schema):
    class Meta:
        fields = ['id', 'user_token', 'items', 'delivery_details', 'subtotal', 'tax', 'total', 'date_placed']

userpayment_schema = UserpaymentShema()
userpayments_schema = UserpaymentShema(many=True)
