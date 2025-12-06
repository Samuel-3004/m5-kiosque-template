from menu import products


def get_products_by_type(type: str):
    products_of_type = []
    for product in products:
        if product["type"] == type:
            products_of_type.append(product)
    return products_of_type
