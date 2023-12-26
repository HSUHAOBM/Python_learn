from flask import render_template, make_response
from flask_restful import Resource, reqparse
from models import db, User

class UserController(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('email', type=str)

    def get(self, user_id=None):
        print('user_id', user_id)

        if user_id is None:
            users = User.query.all()
            html = render_template('users.html', users=users)
            response = make_response(html)
            response.headers['Content-Type'] = 'text/html'
            return response
        else:
            user = User.query.get(user_id)
            return {'id': user.id, 'name': user.name, 'email': user.email}

    # def get(self, user_id=None):
    #     if user_id is None:
    #         users = User.query.all()
    #         return {'users': [{'id': u.id, 'name': u.name, 'email': u.email} for u in users]}
    #     else:
    #         user = User.query.get(user_id)
    #         return {'id': user.id, 'name': user.name, 'email': user.email}

    def post(self):
        args = self.parser.parse_args()
        user = User(name=args['name'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        return {'id': user.id, 'name': user.name, 'email': user.email}

    def put(self, user_id):
        args = self.parser.parse_args()
        user = User.query.get(user_id)
        user.name = args['name']
        user.email = args['email']
        db.session.commit()
        return {'id': user.id, 'name': user.name, 'email': user.email}

    def delete(self, user_id):
        if user_id is None:
            return {'message': 'No user ID specified'}
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}
        db.session.delete(user)
        db.session.commit()
        return {'result': True}