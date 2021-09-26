import os
# import re

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user_resource import UserRegister
from resources.store_resource import Store, StoreList
from resources.item_resource import Item, ItemList


"""
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
"""

app = Flask(__name__)
app.secret_key = "jose"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("postgresql://pmkczqfsbkouje:7d30bf85ef7ecf2dd6c7f888b27381f3cd7d6acc99996e4cf18ec0a3f753e87a@ec2-79-125-30-28.eu-west-1.compute.amazonaws.com:5432/db7spfp41d1bjh", "sqlite:///data.db")
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