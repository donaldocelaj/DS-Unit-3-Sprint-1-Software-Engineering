import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS, rand_name

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability_explode(self):
        """Test stealability method."""
        prod = Product('Test Product', weight=10, price = 10)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...BABOOM!!")

    def test_explode(self):
        """Test Explode method."""
        prod = Product('Test Product', flammability=10, weight=10)
        self.assertEqual(prod.explode(), "...BABOOM!!")

    def test_default_weight(self):
        """Test if product weight is being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    def test_default_num_products(self):
        """Test if products generated is 30."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test all names are legal."""
        products = generate_products()
        names_generated = [i.names_generated for i in products]
        self.assertEqual(set(names_generated) - set(rand_name), set())

if __name__ == '__main__':
    unittest.main()