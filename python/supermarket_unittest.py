import unittest

from model_objects import Product, SpecialOfferType, ProductUnit
from shopping_cart import ShoppingCart
from teller import Teller
from fake_catalog import FakeCatalog

class TestTennis(unittest.TestCase):

    def test_catalog_add_product(self):
        catalog = FakeCatalog()
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        apples = Product("apples", ProductUnit.KILO)

        catalog.add_product(toothbrush, 0.99)
        catalog.add_product(apples, 1.99)

        self.assertEqual({apples, toothbrush}, catalog.products)
        #self.assertEqual(1.99, catalog.unit_price(apples))

    def test_catalog_unit_price(self):
        catalog = FakeCatalog()
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        apples = Product("apples", ProductUnit.KILO)

        catalog.add_product(toothbrush, 0.99)
        catalog.add_product(apples, 1.99)

        self.assertEqual(0.99, catalog.unit_price(toothbrush))
        self.assertEqual(1.99, catalog.unit_price(apples))

    def test_shopping_cart_add_item_quantity(self):
        catalog = FakeCatalog()
        #remplir catalogue


    def test_ten_percent_discount(self):
        catalog = FakeCatalog()
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        apples = Product("apples", ProductUnit.KILO)
        catalog.add_product(toothbrush, 0.99)
        catalog.add_product(apples, 1.99)

        # teller special offers 10% discount on toothbrush
        teller = Teller(catalog)
        teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

        # add apples to shopping cart
        cart = ShoppingCart()
        cart.add_item_quantity(apples, 2.5)

        receipt = teller.checks_out_articles_from(cart)

        # add apples to shopping cart : check no discounts and 1 item
        self.assertEqual([], receipt.discounts)
        self.assertEqual(len(cart.items), len(receipt.items))
        receipt_item = receipt.items[0]
        self.assertEqual(apples, receipt_item.product)
        self.assertEqual(catalog.unit_price(apples), receipt_item.price)
        self.assertEqual(cart.product_quantities[apples], receipt_item.quantity)
        self.assertAlmostEqual(cart.product_quantities[apples] * catalog.unit_price(apples), receipt.total_price(), 0.01)


if __name__ == "__main__":
    unittest.main()