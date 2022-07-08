import random

# AVAILABLE PRODUCTS

products = {
    '0912': {
        'product-name': 'Glue',
        'product-price': 40
    },
    '0913': {
        'product-name': 'Pen',
        'product-price': 20
    },
    '0914': {
        'product-name': 'Notebook',
        'product-price': 60
    },
    '0915': {
        'product-name': 'Pencil',
        'product-price': 10
    }
}

available_items = [product for product in products]

# VARIABLES

cart = {}
item = ''
subtotal = 0

print('\nID   | Cost | Product \n-----------------------')

for product in products:
    product_name = products[product]['product-name']
    product_price = products[product]['product-price']
    print(f'{product} |  {product_price}  | {product_name}')


# CART ITEMS


print("\nEnter Product ID to add product or type 'quit' to exit! \n")

while item != 'quit':

    item = input('Enter Product ID or Exit : ')

    if item in available_items:

        quantity = int(input('Enter Quantity (1 - 10): '))

        if quantity and (0 < quantity <= 10):

            item_name = products[item]['product-name']
            item_price = products[item]['product-price']
            item_summary = {'product-name': item_name, 'product-price': item_price, 'quantity': quantity}
            cart.update({item: item_summary})
        
        else:
            print('Invalid Quantity. Please try again!')

    else:
        print('Product not available!')


# SUBTOTAL CALCULATOR


print('\nYour Cart Subtotal \n')

print('ID   | Qty | Cost | Product \n------------------------------')

for items in cart:
    item_name = cart[items]['product-name']
    item_price = cart[items]['product-price']
    item_quantity = cart[items]['quantity']

    print(f'{items} |  {item_quantity}  |  {item_price}  | {item_name}')

    subtotal += item_price * item_quantity


print(f'\n--- You Subtotal : Rs.{subtotal} ---')


# DISCOUNT CALCULATOR


discount = round(((subtotal * random.randint(5,25)) / 100), 2)
total = subtotal - discount

print(f'\nWe got a surprise for you! Discount coupon of Rs.{discount}')
print(f'\n--- You Total : Rs.{total} ---')