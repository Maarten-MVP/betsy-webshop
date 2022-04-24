from peewee import *
from models import *

def print_search_products(term):
    for result in Product.select().where(Product.name.contains(fn.LOWER(term)) | fn.LOWER(Product.description).contains(fn.LOWER(term))).dicts():
        print(result)


def print_products_of_user(user):
    for product in Product.select(Product.name).join(User).where(User.name == user).dicts():
        print(product)

def print_products_w_tag(tag):
    products = Product.select().join(TaggedProduct).join(ProductTag).where(ProductTag.name == tag).dicts()
    for product in products:
        print(product)

def add_product_to_user(user_id, name, description, price, quantity):
    Product.create(
        user_id = user_id,
        name = name,
        description = description, 
        price = price,
        quantity = quantity
    )

def delete_product_from_user(id):
    q = Product.delete().where(Product.id == id)
    q.execute()

def update_stock(amount, product_id):
    q = Product.update(quantity = Product.quantity + amount).where(Product.id == product_id)
    q.execute()

def handle_purchase(buyer, product_id, quantity):
    Transaction.create(
        buyer = buyer,
        product_id = product_id,
        quantity = quantity,
    )
    update_stock(-quantity, product_id)



def main():
    pass





if __name__ == "__main__":
    main()
