from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TagModel, StoreModel, ItemModel
from schemas import tagSchema, TagAndItemSchema

blp = Blueprint("Tags", "tags", description="Operations on tags")

@blp.route("/store/<string:store_id>/tag")
class TagInStore(MethodView):
    @blp.response(200, tagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()
    
    @blp.arguments(tagSchema)
    @blp.response(201, tagSchema)
    def post(self, tag_data, store_id):
        #name is unique in the tags table so we dont need to check if the tag already exists
        tag = TagModel(**tag_data, store_id=store_id)
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
        return tag

@blp.route("/item/<int:item_id>/tag/<int:tag_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201, tagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)
        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return tag
    
    @blp.response(200,TagAndItemSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)
        item.tags.remove(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
        return {"message":"Tag removed from item successfully.","item":item,"tag":tag}
    

@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):
    @blp.response(200, tagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag
    
    @blp.response(202, description="Delete tag if no item tagged with it", example="Tag deleted successfully.")
    @blp.alt_response(404, description="Tag not found")
    @blp.alt_response(400, description="Tag is linked to an item, tag not deleted")
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        if tag.items.all():
            abort(400, message="Tag is linked to an item, tag not deleted")
        db.session.delete(tag)
        db.session.commit()
        return {"message":"Tag deleted successfully."}

