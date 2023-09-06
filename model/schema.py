from marshmallow import Schema, fields

class Usr(object):
    def __init__(self,name,ap,age,code,nac):
        self.name = name
        self.ap = ap
        self.age = age
        self.code = code
        self.nac = nac

class UsrSchema(Schema):
    name = fields.Str()
    ap = fields.Str()
    age = fields.Int()
    code = fields.Int()
    nac = fields.Str()