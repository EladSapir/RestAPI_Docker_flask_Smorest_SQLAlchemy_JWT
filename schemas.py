from marshmallow import Schema, fields

class PlainitemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainstoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class itemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

class itemSchema(PlainitemSchema):
    store_id = fields.Int(required=True)
    store = fields.Nested(PlainstoreSchema, dump_only=True)

class storeSchema(PlainstoreSchema):
    items= fields.List(fields.Nested(PlainitemSchema), dump_only=True)