from peewee import *

db = SqliteDatabase('betsy_webshop.db')

class BaseModel(Model):
    class Meta:
        database = db

class ProductTag(BaseModel):
    name = CharField(unique=True)

class User(BaseModel):
    name = CharField()
    address_street = CharField()
    address_number = IntegerField()
    address_postal_code = IntegerField()
    address_city = CharField()
    address_country = CharField()
    billing_vat_code = CharField()
    billing_street = CharField()
    billing_number = CharField()
    billing_postal_code = IntegerField()
    billing_city = CharField()
    billing_country = CharField()

class Product(BaseModel):
    user_id = ForeignKeyField(User, backref='products')
    name = CharField(index=True)
    description = CharField(index=True)
    price = DecimalField(auto_round=False)
    quantity = IntegerField()

class TaggedProduct(BaseModel):
    product_id = ForeignKeyField(Product, backref='tags')
    tag_id = ForeignKeyField(ProductTag, backref='products')

class Transaction(BaseModel):
    buyer = CharField()
    product_id = ForeignKeyField(Product)
    quantity = IntegerField()



