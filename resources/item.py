import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import itemSchema, itemUpdateSchema

blp = Blueprint("item", __name__, description="Ops on items")

@blp.route("/item/<string:item_id>")
class Item (MethodView):
    @blp.response(200, itemSchema)
    def get(self,item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    @blp.arguments(itemUpdateSchema)
    @blp.response(200, itemSchema)
    def put(self,item_data,item_id):
        try:
            item = items[item_id]
            item|=item_data
            return item

        except KeyError:
            abort(404, message="Item not found.")

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, itemSchema(many=True))
    def get(self):
        return items.values()
    
    @blp.arguments(itemSchema)
    @blp.response(201, itemSchema)
    def post(self, item_data):
        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message=f"Item already exists.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item