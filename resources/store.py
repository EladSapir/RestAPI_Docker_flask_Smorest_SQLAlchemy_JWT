import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import storeSchema

blp = Blueprint("stores", __name__, description="Ops on stores")

@blp.route("/store/<string:store_id>")
class Store (MethodView):
    @blp.response(200, storeSchema)
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")


@blp.route("/store")
class Stores (MethodView):

    @blp.arguments(storeSchema)
    @blp.response(201, storeSchema)
    def post(self,store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store already exists.")

        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store

        return store
    
    @blp.response(200, storeSchema(many=True))
    def get(self):
        return stores.values()