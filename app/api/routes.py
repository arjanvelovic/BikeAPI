from flask import Blueprint, request, jsonify
from models import db, User, user_schema, users_schema, Bikeconfig, bike_config_schema, bikes_config_schema, Usercart, usercart_schema, usercarts_schema, Userpayment, userpayment_schema, userpayments_schema

from flask import request
from models import db, Bikeconfig, User
from ..auth.routes import basic_auth

api = Blueprint('api',__name__, url_prefix='/api')

# Delete ALL DATA
# @api.route('/deletedata', methods = ['DELETE'])
# def delete_all():
#     users = User.query.all()
#     bikeconfigs = Bikeconfig.query.all()
#     carts = Usercart.query.all()
#     payments = Userpayment.query.all()
#     for user in users:
#         db.session.delete(user)
#     for bikeconfig in bikeconfigs:
#         db.session.delete(bikeconfig)
#     for cart in carts:
#         db.session.delete(cart)
#     for payment in payments:
#         db.session.delete(payment)
#     db.session.commit()
#     return jsonify('All data has been deleted')


##############################################################################

# Endpoint to get token - requires email/password/ signin
@api.route('/token', methods = ['GET'])
@basic_auth.login_required
def get_user_token():
    auth_user = basic_auth.current_user()
    token = auth_user.get_token()
    return {'token': token}

# Create user/signup
@api.route('/user', methods = ['POST'])
def create_user():
    isAdmin = request.json['isAdmin']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    phone_number = request.json['phone_number']
    address_street = request.json['address_street']
    address_city = request.json['address_city']
    address_state = request.json['address_state']
    address_zipcode = request.json['address_zipcode']

    user = User(isAdmin, first_name, last_name, email, password, phone_number, address_street, address_city, address_state, address_zipcode)

    db.session.add(user)
    db.session.commit()

    response = user_schema.dump(user)
    return jsonify(response)

# Create mock users
# @api.route('/mockusers', methods = ['POST'])
# def create_mock_users():
#     emails = ['test0@gmail.com', 'test1@gmail.com', 'test2@gmail.com']
#     for i in range(len(emails)):
#         isAdmin = False
#         first_name = i
#         last_name = i
#         email = emails[i]
#         password = 'gogoli12'
#         phone_number = i
#         address_street = i
#         address_city = i
#         address_state = i
#         address_zipcode = i

#         user = User(isAdmin, first_name, last_name, email, password, phone_number, address_street, address_city, address_state, address_zipcode)
#         db.session.add(user)

#     db.session.commit()
#     return jsonify('Mock users were added')

# Get all users
# @api.route('/users', methods = ['GET'])
# def get_all_users():
#     users = User.query.all()
#     response = users_schema.dump(users)
#     return jsonify(response)

#Get User Info
@api.route('/user/<token>', methods = ['GET'])
def get_user_info(token):
    auth_user = User.query.filter_by(token=token).first()
    response = user_schema.dump(auth_user)
    return jsonify(response)

#Update User info
@api.route('/user/<token>', methods = ['PUT'])
def update_user_info(token):
    auth_user = User.query.filter_by(token=token).first()

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone_number = request.json['phone_number']
    address_street = request.json['address_street']
    address_city = request.json['address_city']
    address_state = request.json['address_state']
    address_zipcode = request.json['address_zipcode']

    auth_user.first_name = first_name
    auth_user.last_name = last_name
    auth_user.phone_number = phone_number
    auth_user.address_street = address_street
    auth_user.address_city = address_city
    auth_user.address_state = address_state
    auth_user.address_zipcode = address_zipcode

    db.session.commit()

    response = user_schema.jsonify(auth_user)
    return response

# Delete User
# @api.route('/user/<token>', methods = ['DELETE'])
# def delete_user(token):
#     auth_user = User.query.filter_by(token=token).first()
#     db.session.delete(auth_user)
#     db.session.commit()
#     return user_schema.jsonify(auth_user)

# Delete All Users
# @api.route('/deleteusers', methods = ['DELETE'])
# def delete_all_users():
#     users = User.query.all()
#     for user in users:
#         db.session.delete(user)
#     db.session.commit()
#     return users_schema.jsonify(users)

#############################################################################

# Create Bikeconfig
@api.route('/bikeconfig', methods = ['POST'])
def create_bikeconfig():
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    color = request.json['color']
    trim = request.json['trim']
    category = request.json['category']
    size = request.json['size']
    cost = request.json['cost']

    bikeconfig = Bikeconfig(make, model, year, color, category, trim, size, cost)

    db.session.add(bikeconfig)
    db.session.commit()

    response = bike_config_schema.dump(bikeconfig)
    return jsonify(response)

# Create All Bike Configs
# @api.route('/bikeconfigs', methods = ['POST'])
# def create_all_bikeconfigs():

#     allbikes = {
#         'make': 'Specialized',
#         'year': '2024',
#         'category':{
#             'Road': {
#                 'Allez': {
#                     'colors' : ['Smoke', 'Lagoon Blue', 'Maroon'],
#                     'sizes' : [49, 52, 54, 56, 58, 61],
#                     'trims' : {
#                         'Base': 1200.00,
#                         'Elite': 1700.00,
#                         'Sport': 1800.00,
#                         'Sprint Comp': 3000.00,
#                         'Sprint LTD': 3500.00
#                     }
#                 },
#                 'Tarmac': {
#                     'colors' : ['Ghost Pearl', 'Black', 'Pine Green'],
#                     'sizes' : [49, 52, 54, 56, 58, 61],
#                     'trims' : {
#                         'SL6': 2500.00,
#                         'SL6 Sport': 3500.00,
#                         'SL7 Sport': 3800.00,
#                         'SL7 Expert': 6500.00,
#                         'SL8 Expert': 6500.00,
#                         'SL8 Pro': 8500.00
#                     }
#                 },
#                 'Roubaix': {
#                     'colors' : ['Smoke', 'UV Lilac', 'Doppio'],
#                     'sizes' : [49, 52, 54, 56, 58, 61],
#                     'trims' : {
#                         'Base': 2700.00,
#                         'SL8': 2800.00,
#                         'Sport': 3500.00,
#                         'SL8 Expert': 6500.00,
#                         'SL8 Pro': 8500.00
#                     }
#                 },
#                 'Diverge': {
#                     'colors' : ['Birch', 'Redwood', 'Midnight Shadow'],
#                     'sizes' : [49, 52, 54, 56, 58, 61],
#                     'trims' : {
#                         'E5': 1300.00,
#                         'Elite E5': 2000.00,
#                         'Comp E5': 2500.00,
#                         'Sport Carbon': 3000.00,
#                         'Comp Carbon': 4000.00
#                     }
#                 },
#                 'Crux': {
#                     'colors' : ['Gloss Vivid Pink', 'Satin Taupe'],
#                     'sizes' : [49, 52, 54, 56, 58, 61],
#                     'trims' : {
#                         'Comp': 4000.00,
#                         'Expert': 6200.00,
#                         'Pro': 8200.00,
#                     }
#                 },
#             },
#             'Mountain': {
#                 'Rockhopper': {
#                     'colors' : ['Tarmac Black', 'Flo Red', 'Cast Blue Metallic'],
#                     'sizes' : ['XS', 'S', 'M', 'L', 'XL'],
#                     'trims' : {
#                         '29': 650.00,
#                         'Sport': 750.00,
#                         'Comp': 950.00,
#                         'Expert': 1300.00
#                     }
#                 },
#                 'Sumpjumper': {
#                     'colors' : ['Black', 'Blaze', 'White Sage'],
#                     'sizes' : ['XS', 'S', 'M', 'L', 'XL'],
#                     'trims' : {
#                         'Alloy': 2800.00,
#                         'Comp': 5000.00,
#                         'EVO Expert': 6300.00,
#                         'EVO Pro': 8600.00,
#                         'S-Works': 11000.00
#                     }
#                 },
#                 'Demo': {
#                     'colors' : ['Desert Rose', 'Metallic Dark Navy'],
#                     'sizes' : ['XS', 'S', 'M', 'L', 'XL'],
#                     'trims' : {
#                         'Expert': 5600.00,
#                         'Race': 7100.00,
#                     }
#                 },
#                 'Epic': {
#                     'colors' : ['Birch', 'Redwood', 'Midnight Shadow'],
#                     'sizes' : ['XS', 'S', 'M', 'L', 'XL'],
#                     'trims' : {
#                         'Hardtail': 2500.00,
#                         'Hardtail Comp': 3200.00,
#                         'Hardtail Expert': 4500.00,
#                         'Hardtail Pro': 5800.00,
#                         'Hardtail S-Works': 11000.00
#                     }
#                 },
#                 'Fuse': {
#                     'colors' : ['Doppio', 'Artic Blue', 'Cast Blue', 'Terra Cotta'],
#                     'sizes' : ['XS', 'S', 'M', 'L', 'XL'],
#                     'trims' : {
#                         '27.5': 1500.00,
#                         'Sport 27.5': 2400.00,
#                         'Expert 29': 2900.00,
#                         'Comp 29': 3000.00,
#                     }
#                 },
#             },
#             'Active': {
#                 'Sirrus': {
#                     'colors' : ['Black', 'Cool Grey', 'Sky Blue', 'Fiery Red'],
#                     'sizes' : ['XS', 'S', 'M', 'L', 'XL'],
#                     'trims' : {
#                         '1.0': 650.00,
#                         '2.0': 775.00,
#                         '3.0': 1200.00,
#                         '4.0': 1500.00,
#                         '6.0': 3000.00,
#                     }
#                 },
#                 'Roll': {
#                     'colors' : ['Lagoon Blue', 'Cool Grey', 'Tarmac Black', 'Redwood'],
#                     'sizes' : ['XS', 'S', 'M', 'L', 'XL'],
#                     'trims' : {
#                         '2.0': 700.00,
#                         '2.0 Low Entry': 700.00,
#                         '3.0': 1100.00,
#                         '3.0 Low Entry': 1100.00
#                     }
#                 },
#                 'Turbo Vado': {
#                     'colors' : ['Cast Black', 'White Mountains', 'Red Tint'],
#                     'sizes' : ['XS', 'S', 'M', 'L', 'XL'],
#                     'trims' : {
#                         '3.0': 3250.00,
#                         '4.0': 4000.00,
#                         '5.0': 5000.00,
#                     }
#                 }
#             }
#         }
#     }

#     make = allbikes['make']
#     year = allbikes['year']

#     for category in allbikes['category']:
#         for model in allbikes['category'][category]:
#             for color in allbikes['category'][category][model]['colors']:
#                 for size in allbikes['category'][category][model]['sizes']:
#                     for trim in allbikes['category'][category][model]['trims']:
#                         cost = allbikes["category"][category][model]["trims"][trim]

#                         bikeconfig = Bikeconfig(make, model, year, color, category, trim, size, cost)
#                         db.session.add(bikeconfig)
                                 
#     db.session.commit()                    
#     bikes = Bikeconfig.query.all()
#     response = bikes_config_schema.dump(bikes)
#     return jsonify(response)

# Get all Vehicle Configs
@api.route('/bikeconfigs', methods = ['GET'])
def get_all_bikeconfigs():
    bikeconfigs = Bikeconfig.query.all()
    response = bikes_config_schema.dump(bikeconfigs)
    return jsonify(response)

# Get Single Bike Config
@api.route('/bikeconfig/<id>', methods = ['GET'])
def get_bikeconfig(id):
    bikeconfig = Bikeconfig.query.get(id)
    return bike_config_schema.jsonify(bikeconfig)

# Delete All Bike Config
# @api.route('/deletebikes', methods = ['DELETE'])
# def delete_all_bikeconfigs():
#     bikeconfigs = Bikeconfig.query.all()
#     for bikeconfig in bikeconfigs:
#         db.session.delete(bikeconfig)
#     db.session.commit()
#     return bikes_config_schema.jsonify(bikeconfigs)


#########################################################################

# Add Bike to Cart by Search
@api.route('/usercart/<token>', methods = ['POST'])
def add_to_cart(token):

    model = request.json['model']
    color = request.json['color']
    trim = request.json['trim']
    size = request.json['size']

    bike = Bikeconfig.query.filter_by(model=model, color=color, trim=trim, size=size).first()

    quantitysubmitted = request.json['quantity']
    bike_id = bike.id
    user_token = token
    cost = bike.cost

    if Usercart.query.filter_by(user_token=token, bike_id=bike_id).first():
        cartitem = Usercart.query.filter_by(user_token=token, bike_id=bike_id).first()
        cartitem.quantity += quantitysubmitted
        cartitem.itemtotal = cost * cartitem.quantity

    else:
        itemtotal = cost * quantitysubmitted
        cartitem = Usercart(user_token, bike_id, quantitysubmitted, itemtotal)
        db.session.add(cartitem)

    db.session.commit()

    response = usercart_schema.dump(cartitem)
    return jsonify(response)

# Add Bike to Cart by ID
@api.route('/usercartid/<token>', methods = ['POST'])
def add_bike_to_cartid(token):

    quantitysubmitted = request.json['quantity']
    bike_id = request.json['bike_id']
    user_token = token

    bike = Bikeconfig.query.filter_by(id=bike_id).first()
    cost = bike.cost

    if Usercart.query.filter_by(user_token=token, bike_id=bike_id).first():
        cartitem = Usercart.query.filter_by(user_token=token, bike_id=bike_id).first()
        cartitem.quantity += quantitysubmitted
        cartitem.itemtotal = cost * cartitem.quantity

    else:
        itemtotal = cost * quantitysubmitted
        cartitem = Usercart(user_token, bike_id, quantitysubmitted, itemtotal)
        db.session.add(cartitem)

    db.session.commit()

    response = usercart_schema.dump(cartitem)
    return jsonify(response)

# Get User Cart
@api.route('/usercart/<token>', methods = ['GET'])
def user_cart(token): 
    usercart = Usercart.query.filter_by(user_token=token).all()
    response = []
    for item in usercart:
        bikeconfig = bike_config_schema.dump(Bikeconfig.query.filter_by(id=item.bike_id).first())
        bikeconfig['cart_id'] = item.id
        bikeconfig['quantity'] = item.quantity
        bikeconfig['cart_itemtotal'] = item.itemtotal

        response.append(bikeconfig)

    return jsonify(response)

# Delete Item from cart
@api.route('/usercart/<id>', methods = ['DELETE'])
def delete_item_from_cart(id):
    item = Usercart.query.filter_by(id=id).first()
    db.session.delete(item)
    db.session.commit()
    return usercart_schema.jsonify(item)

# Update Cart Item
@api.route('/usercart/<id>', methods = ['PUT'])
def update_cart_item(id):
    cartitem = Usercart.query.filter_by(id=id).first()

    bike = Bikeconfig.query.filter_by(id=cartitem.bike_id).first()
    cost = bike.cost

    quantity = request.json['quantity']
    cartitem.quantity = quantity
    cartitem.itemtotal = quantity * cost

    db.session.commit()
    return usercart_schema.jsonify(cartitem)

# Clear User Cart
@api.route('/clearcart/<token>', methods = ['DELETE'])
def clear_cart(token):
    usercart = Usercart.query.filter_by(user_token=token).all()
    for item in usercart:
        db.session.delete(item)
    db.session.commit()
    return jsonify(f'User: {token} cart has been cleared')

# Delete All Carts
# @api.route('/deletecarts', methods = ['DELETE'])
# def delete_carts():
#     carts = Usercart.query.all()
#     for cart in carts:
#         db.session.delete(cart)
#     db.session.commit()
#     return usercarts_schema.jsonify(carts)

#####################################################################################

# Add Complete Payment
@api.route('/userpayment/<token>', methods = ['POST'])
def add_complete_payment(token):
    user_token = token
    items = request.json['items']
    delivery_details = request.json['delivery_details']
    subtotal = request.json['subtotal']
    tax = request.json['tax']
    total = subtotal + tax

    userpayment = Userpayment(user_token, items, delivery_details, subtotal, tax, total)
    db.session.add(userpayment)
    db.session.commit()

    response = userpayment_schema.dump(userpayment)
    return jsonify(response)

# Get User Payments
@api.route('/userpayments/<token>', methods = ['GET'])
def get_user_payments(token):
    userpayments = Userpayment.query.filter_by(user_token=token).all()
    response = userpayments_schema.dump(userpayments)
    return jsonify(response)

# Get Single Payment
@api.route('/userpayment/<id>', methods = ['GET'])
def get_single_payment(id):
    payment = Userpayment.query.filter_by(id=id).first()
    response = userpayment_schema.dump(payment)
    return jsonify(response)

# Delete all Payments
# @api.route('/deletepayments', methods = ['DELETE'])
# def delete_all_payments():
    payments = Userpayment.query.all()
    for payment in payments:
        db.session.delete(payment)
    db.session.commit()
    return userpayments_schema.jsonify(payments)