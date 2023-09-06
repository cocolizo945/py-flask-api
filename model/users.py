from marshmallow import post_load

from .schema import Usr,UsrSchema

class User_crud(Usr):
    def __init__(self,name,ap,age,code,nac):
        super(User_crud, self).__init__(name,ap,age,code,nac)


class User_crudSchema(UsrSchema):
    @post_load
    def make_UsrCrud(self, data, **kwargs):
        return User_crud(**data)
