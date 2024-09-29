orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Chuck", "iPhone", 1),
    ("Ashley", "Books", 5 )
]
def customer_order_info(orders):
    for order_info in orders:
        customer, product, quantity = order_info
        print(f"Customer: {customer} \nPurchase: {product} \nQuantity: {quantity}")

customer_order_info(orders)