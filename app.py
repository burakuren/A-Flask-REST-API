import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user_resource import UserRegister
from resources.store_resource import Store, StoreList
from resources.item_resource import Item, ItemList

app = Flask(__name__)
app.secret_key = "jose"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL_NEW")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

api.add_resource(UserRegister, "/register")


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)