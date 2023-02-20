from flask_restful import Resource, reqparse
from models import db, User


class UserController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name is required', required=True)
    parser.add_argument('age', type=int, help='Age is required', required=True)

    def get(self, user_id=None):
        """
        Get user(s) by id or get all users.

        ---
        tags:
          - Users
        parameters:
          - name: user_id
            in: path
            type: integer
            required: false
            description: The ID of the user to retrieve.
        responses:
          200:
            description: Returns a user or a list of users.
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: The user ID.
                name:
                  type: string
                  description: The user name.
                age:
                  type: integer
                  description: The user age.
          404:
            description: The requested user was not found.
        """
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {'message': 'User not found'}, 404
            return {'id': user.id, 'name': user.name, 'age': user.age}
        else:
            users = User.query.all()
            return [{'id': user.id, 'name': user.name, 'age': user.age} for user in users]

    def post(self):
        """
        Add a new user
        ---
        tags:
          - User
        parameters:
          - name: username
            in: formData
            type: string
            required: true
            description: Username of the user to create
          - name: email
            in: formData
            type: string
            required: true
            description: Email address of the user to create
        responses:
          201:
            description: User created
            schema:
              id: User
              properties:
                id:
                  type: integer
                  description: The user ID
                  default: 1
                username:
                  type: string
                  description: The username
                  default: john.doe
                email:
                  type: string
                  description: The email address
                  default: john.doe@example.com
          400:
            description: Missing required parameter(s)
        """
        data = UserController.parser.parse_args()
        user = User(name=data['name'], age=data['age'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully', 'id': user.id}, 201

    def put(self, user_id):
        """
        Update user information by user_id
        ---
        tags:
          - User
        parameters:
          - name: user_id
            in: path
            type: integer
            required: true
            description: ID of user to update
          - name: username
            in: formData
            type: string
            required: false
            description: Username of the user to update
          - name: email
            in: formData
            type: string
            required: false
            description: Email address of the user to update
        responses:
          200:
            description: User information updated
            schema:
              id: User
              properties:
                id:
                  type: integer
                  description: The user ID
                  default: 1
                username:
                  type: string
                  description: The username
                  default: john.doe
                email:
                  type: string
                  description: The email address
                  default: john.doe@example.com
          404:
            description: User not found
        """
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        data = UserController.parser.parse_args()
        user.name = data['name']
        user.age = data['age']
        db.session.commit()
        return {'message': 'User updated successfully', 'id': user.id}

    def delete(self, user_id):
        """
        Delete user by user_id
        ---
        tags:
          - User
        parameters:
          - name: user_id
            in: path
            type: integer
            required: true
            description: ID of user to delete
        responses:
          204:
            description: User deleted
          404:
            description: User not found
        """
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully', 'id': user.id}