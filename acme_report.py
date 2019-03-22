from acme import Product, BoxingGlove
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
rand_price = random.randint(5,100)
rand_weight = random.randint(5,100)
rand_flam = random.uniform(0,2.5)
rand_name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)

def generate_products(products=30):
    supply =[]
    for i in range(0,products):
         product= Product(name = rand_name, price=rand_price, 
                          weight=rand_weight, flammability=rand_flam)
         supply.append(product)
    return supply

supply = generate_products()

def inventory_report(inventory):
    length = len(inventory)
    print('there are ' + str(length) + ' products')
    weight = 0
    price = 0
    flammability = 0
    for i in range(0, length):
        weight += inventory[i].weight
        price += inventory[i].price
        flammability += inventory[i].flammability
    mean_weight = weight / length
    mean_price = price / length
    mean_flam = flammability / length
    print('The average weight is ' + str(weight) + ' pounds')
    print('The average price is $' + str(price))
    print('the average flammability is ' + str(flammability))

if __name__ == '__main__':
    inventory_report(generate_products())