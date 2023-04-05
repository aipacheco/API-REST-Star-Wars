from flask import request, jsonify
from models.index import db, User
import domain.user.controller as Controller

def user_route(app):

    @app.route('/user', methods=['GET'])
    def get_users():
        all_users = User.query.all()
        # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
        user_serialized = list(
            map(lambda planet: user.serialize(), all_users))
        return planet_serialized


    @app.route('/user/<int:id>', methods=['GET'])
    def get_single_user(id):  # el id se pasa como param de la funcion
        # para llamar al id se llama a la clase user, metodo query.get pasandole el id como param
        user = User.query.get(id)
        return jsonify(user.serialize()), 200


    @app.route('/user', methods=['POST'])
    def create_user():
        data = request.get_json()
        user = user(user_name=data['user_name'],  # Agrega el nombre del user
                    password=data['password'],
                    name=data['name'],
                    last_name=data['last_namelast_name'],
                    email=data['email']
                    )
        db.session.add(user)
        db.session.commit()

        response = {
            "result": {
                "user": user.serialize(),
            }
        }
        return response, 201


    @app.route('/user/<int:id>', methods=['PUT'])
    def modify_user(id):
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'El user no existe'}), 404

        data = request.get_json()
        user.user_name = data['user_name']
        user.password = data['password']
        user.name = data['name']
        user.last_name = data['last_name']
        user.email = data['email']

        db.session.commit()

        return jsonify(user.serialize()), 200


    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
        user = user.query.get(id)
        if not user:
            return jsonify({'error': 'El user no existe'}), 404

        db.session.delete(user)
        db.session.commit()

        return '', 204