from marshmallow import Schema, fields

class PlainitemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainstoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainTagSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class itemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

class itemSchema(PlainitemSchema):
    store_id = fields.Int(required=True)
    store = fields.Nested(PlainstoreSchema, dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema), dump_only=True)

class storeSchema(PlainstoreSchema):
    items= fields.List(fields.Nested(PlainitemSchema), dump_only=True)
    tags= fields.List(fields.Nested(PlainTagSchema), dump_only=True)

class tagSchema(PlainTagSchema):
    store_id = fields.Int(dump_only=True)
    store = fields.Nested(PlainstoreSchema, dump_only=True)
    items = fields.List(fields.Nested(PlainitemSchema), dump_only=True)

class TagAndItemSchema(Schema):
    messasge = fields.Str()
    item = fields.Nested(itemSchema)
    tag = fields.Nested(tagSchema)

class UserSchema(Schema):
    id = fields.Int(dump_only=True) # dump_only - will be created by database and not sent by user
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True) # load_only - will not be sent by user