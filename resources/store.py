import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import storeSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import StoreModel

blp = Blueprint("stores", __name__, description="Ops on stores")

@blp.route("/store/<int:store_id>")
class Store (MethodView):
    @blp.response(200, storeSchema)
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit() 
        return {"message":"Store deleted successfully."}


@blp.route("/store")
class Stores (MethodView):

    @blp.arguments(storeSchema)
    @blp.response(201, storeSchema)
    def post(self,store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="An error occurred while creating the store.(name exists)")
        except SQLAlchemyError:
            abort(400, message="An error occurred while creating the store.")


        return store
    
    @blp.response(200, storeSchema(many=True))
    def get(self):
        return StoreModel.query.all()