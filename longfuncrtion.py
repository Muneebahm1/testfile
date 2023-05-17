def calculate_total_price(items):
    # Long and complex function with multiple responsibilities
    total_price = 0
    for item in items:
        price = item['price']
        quantity = item['quantity']
        discount = item['discount']
        shipping_cost = item['shipping_cost']
        
        subtotal = price * quantity
        subtotal -= discount
        subtotal += shipping_cost
        
        total_price += subtotal
        
    return total_price
