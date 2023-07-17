from . import user_blueprint
from app.models import User
from app import db
import uuid
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@user_blueprint.route('/test', methods=['GET','POST'])
def ttest():    
    return jsonify({'tasks': tasks})



@user_blueprint.route('/me', methods=['GET'])
@jwt_required
def get_me():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=uuid.UUID(current_user_id)).first_or_404()
    response_data = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'created_at': user.created_at
    }
    return jsonify(response_data), 200

@user_blueprint.route('/me', methods=['PUT'])
@jwt_required
def update_me():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=uuid.UUID(current_user_id)).first_or_404()
    data = request.get_json()
    user.first_name = data.get("first_name", "")
    user.last_name = data.get("last_name", "")
    db.session.add(user)
    db.session.commit()
    response_data = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'created_at': user.created_at
    }
    return jsonify(response_data), 201
