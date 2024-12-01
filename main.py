def show_inventory():
    print()
    for product, data in inventory.items():
        print(f'{product.upper()} ===> Price: R${data[0]:.2f}; Quantity: {data[1]:.2f}')
    print()

def register():
    if (inventory):
        show_inventory()
    else:
        print()

    while True:
        try:
            product = input('Enter the product name: ')
            price = float(input('Enter the product price: '))
            quantity = int(input('Enter the product quantity: '))

            product_verified = product.lower().strip()

            if product_verified in inventory:
                inventory[product_verified][1] += quantity
            else:
                inventory[product_verified] = [price, quantity]

        except KeyError:
            print('Invalid product! Try again.\n')
            continue
        except ValueError:
            print('Error! Try again.\n')
            continue
        else:
            print('\nProduct added successfully!\n')
            break

def buy():
    orders = []

    show_inventory()

    while True:
        try:
            product = input('Enter the product name: ')
            quantity = int(input('Enter the product quantity: '))

            product_verified = product.lower().strip()

            if inventory[product_verified][1] >= quantity:
                inventory[product_verified][1] -= quantity
                orders.append([product_verified, quantity])
            else:
                print('Invalid quantity. Try again.\n')
                continue
            
        except KeyError:
            print('Invalid product! Try again.\n')
            continue
        except ValueError:
            print('Error! Try again.\n')
            continue
        else:
            finish = input('Do you want to continue? [S/N] ')
            print()
            if finish.lower() == 'n':
                break
    
    total = 0
    for item in orders:
        product = item[0]
        quantity = item[1]
        price = inventory[product][0]
        total_product = item[1] * price

        print(f'{product} ===> {quantity} x R${price} = R${total_product}')
        total += total_product

    print(f'Total to pay: R${total:.2f}')

    show_inventory()


# Main Program

inventory = {}

while True:
    print('-' * 30 + ' Menu ' + '-' * 30)
    print('1-Register | 2-Buy | 3-Close the program\n')
    choose = int(input('Enter your choose here: '))

    match choose:
        case 1:
            register()
        case 2:
            buy()
        case 3:
            print('Closing the program...')
            break
        case _:
            print('Invalid option! Try again.\n')
            continue
