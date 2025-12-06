from management.product_handle.get_product_by_id import get_product_by_id
from management.product_handle.get_products_by_type import get_products_by_type


if __name__ == "__main__":
    # Seus prints de teste aqui
    resultado_product_id = get_product_by_id(28)
    resultado_product_type = get_products_by_type("drink")
    #  print(resultado_product_id)
    print(resultado_product_type)
