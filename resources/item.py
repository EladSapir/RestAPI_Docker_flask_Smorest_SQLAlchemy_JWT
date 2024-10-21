from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from schemas import itemSchema, itemUpdateSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError
from models import ItemModel

blp = Blueprint("item", __name__, description="Ops on items")

@blp.route("/item/<int:item_id>")
class Item (MethodView):
    @jwt_required()
    @blp.response(200, itemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
    
    @jwt_required()
    def delete(self,item_id):
        jwt = get_jwt()
        if not jwt["is_admin"]:
            abort(401, message="Admin privilege required.")
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message":"Item deleted successfully."}
    
    @jwt_required()
    @blp.arguments(itemUpdateSchema)
    @blp.response(200, itemSchema)
    def put(self,item_data,item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()
        return item
        

@blp.route("/item")
class ItemList(MethodView):
    @jwt_required()
    @blp.response(200, itemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    
    @jwt_required()
    @blp.arguments(itemSchema)
    @blp.response(201, itemSchema)
    def post(self, item_data):
    
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, message="An error occurred while adding the item.")


        return item