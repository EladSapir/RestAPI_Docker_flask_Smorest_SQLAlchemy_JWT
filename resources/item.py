import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import itemSchema, itemUpdateSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError
from models import ItemModel

blp = Blueprint("item", __name__, description="Ops on items")

@blp.route("/item/<string:item_id>")
class Item (MethodView):
    @blp.response(200, itemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message":"Item deleted successfully."}

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
    @blp.response(200, itemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    
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