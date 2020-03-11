from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from user import User, UserRegister
from item import Item, ItemList
from pet import Pet, PetList


app = Flask(__name__)
app.secret_key = 'password'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# items = []
# pets = []
# users = []

# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price', type=float, required=True, help="Do not leave blank!")

#     #@jwt_required()
#     def get(self, name):
#         return {'item': next(filter(lambda x: x['name'] == name, items), None)}

#     #@jwt_required()
#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, items), None) is not None:
#             return {'message': "An item with the name '{}' already exisits.". format(name)}

#         data = Item.parser.parse_args()

#         item = {'name': name, 'price': data['price']}
#         items.append(item)
#         return item

#     #@jwt_required()
#     def delete(self, name):
#         global items
#         items = list(filter(lambda x: x['name'] == name, items), None)
#         return {'message': 'Item deleted'}

#     #@jwt_required()
#     def put(self, name):
#         data = Item.parser.parse_args()
#         item = next(filter(lambda x: x['name'] == name, items), None)
#         if item is None:
#             item = {'name': name, 'price': data['price']}
#             items.append(item)
#         else:
#             item.update(data)
#         return item

# class ItemList(Resource):
    
#     #@jwt_required()
#     def get(self):
#         return {'items': items}


# class Pet(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price', type=float, required=True, help="Do not leave blank!")

#     @jwt_required()
#     def get(self, name):
#         return {'pet': next(filter(lambda x: x['name'] == name, pets), None)}

#     #@jwt_required()
#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, pets), None) is not None:
#             return {'message': "A pet with the name '{}' already exisits.". format(name)}

#         data = Pet.parser.parse_args()

#         pet = {'name': name, 'price': data['price']}
#         pets.append(pet)
#         return pet

#     #@jwt_required()
#     def delete(self, name):
#         global pets
#         pets = list(filter(lambda x: x['name'] == name, pets), None)
#         return {'message': 'Pet deleted'}

#     #@jwt_required()
#     def put(self, name):
#         data = Pet.parser.parse_args()
#         pet = next(filter(lambda x: x['name'] == name, pets), None)
#         if pet is None:
#             pet = {'name': name, 'price': data['price']}
#             pets.append(pet)
#         else:
#             pet.update(data)
#         return pet

# class PetList(Resource):
    
#     #@jwt_required()
#     def get(self):
#         return {'pets': pets}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Pet, '/pet/<string:name>')
api.add_resource(PetList, '/pets')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
