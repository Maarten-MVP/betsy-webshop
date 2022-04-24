from models import *

def populate_test_data():
    db.connect()
    db.create_tables([ProductTag, Product, User, Transaction, TaggedProduct])

    product_tags = ['real estate', 'hard ware', 'toys', 'animals']
    for tag in product_tags:
        ProductTag.create(name = tag)
    
    users = {
        'Maarten': ['Straatweg', 30, 9000, 'Gent', 'België', 'BE0534.924.703', 'Wegstraat', 32, 9000, 'Gent', 'België'],
        'Jonas': ['Weglaan', 18, 8000, 'Brugge', 'België', 'BE0534.924.600', 'Baanweg', 62, 8000, 'Brugge', 'België']
    }
    for key, value in users.items():
        User.create(
            name = key,
            address_street = value[0],
            address_number = value[1],
            address_postal_code = value[2],
            address_city = value[3],
            address_country = value[4],
            billing_vat_code = value[5],
            billing_street = value[6],
            billing_number = value[7],
            billing_postal_code =value[8],
            billing_city = value[9],
            billing_country = value[10],
        )
    
    products = [
        [1, 'Game Boy', 'Restored Game Boy from 1995', 55.60, 10,],
        [1, 'Sword', 'Wooden Sword', 12.5, 10,],
        [1, 'Horse', 'A great horse', 500, 1,],
        [1, 'House', 'Newly restored house', 550000, 1,],
    ]
    for value in products:
        Product.create(
            user_id = value[0],
            name = value[1],
            description = value[2],
            price = value[3],
            quantity = value[4],
        )

    tagged_products = {
        1:2,
        2:3,
        3:4,
        4:1
    }
    for key, value in tagged_products.items():
        TaggedProduct.create(
            product_id = key,
            tag_id = value
        )

    db.close()

populate_test_data()
