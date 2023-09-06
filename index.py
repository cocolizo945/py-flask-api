from flask import Flask, jsonify, request
import sys
sys.path.append(",/model")

from model.users import User_crud, User_crudSchema

app = Flask(__name__)

users = [
    User_crud('juan','martinez',20,364,'mexico')
]

@app.route('/users')
def get_users():
    schema = User_crudSchema(many=True)
    user = schema.dump(users)
    return jsonify(user)

@app.route('/users', methods=['POST'])
def add_users():
    user = User_crudSchema().load(request.get_json())
    users.append(user)
    print(users)
    return "", 204

if __name__ == "__main__":
    app.run()