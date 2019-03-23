import random
rand = random.randint(1000000, 9999999)
class Product:
    """ A class for all the products in Acme"""
    def __init__(self, name=None, price=10, weight=20, flammability=0.5, identifier = rand):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Report how likely a product is to be stolen"""
        ratio = self.price / self.weight
        if ratio < .5:
            return 'Not so stealable...'
        elif ratio < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'
    
    def explode(self):
        """Report how likely a product is to explode"""
        ratio = self.flammability*self.weight
        if ratio < 10:
            return '...fizzle'
        elif 10 <= ratio < 50:
            return '...boom' 
        else:
            return '...BABOOM!!'

class BoxingGlove(Product):
    """One of the products sold at Acme"""
    def __init__(self, name=None, price=10, flammability=0.5, identifier = rand):  
        super().__init__(weight=10)

