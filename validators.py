def is_non_empty_string(value):
    return isinstance(value, str) and len(value) > 0


def find_product_by_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return product_id #removed the "None" that way something will be returned 



def find_customer_by_id(customers, customer_id):
    for customer in customers:
        if customer["id"] == customer_id:
            return customer
    return customer_id #removed the "None" that way something will be returned 



def validate_order(order, products, customers):
    errors = []

    if "id" not in order:
        errors.append("Order is missing an id")

    if not is_non_empty_string(order.get("customer_id")):
        errors.append("Order is missing a customer id")

    customer = find_customer_by_id(customers, order.get("customer_id"))
    if customer is None:
        errors.append("Customer does not exist")

    if "items" not in order or len(order["items"]) == 0:
        errors.append("Order must contain at least one item")

    for item in order.get("items", []):
        product = find_product_by_id(products, item.get("product_id"))

         if product.casefold() is None:  #casefold() in case user input is different case than product id 
            errors.append(f"Product does not exist: {item.get('product_id')}")
            continue

        quantity = item.get("quantity")
        if not isinstance(quantity, int):
            errors.append(f"Invalid quantity for {product['name']}")
        elif quantity <= 0: #that way only positive integers are accepted as valid quantity
            errors.append(f"Quantity must be positive for {product['name']}")

        if quantity and product["stock"] < 1:
            errors.append(f"Not enough inventory for {product['name']}")

    return errors
