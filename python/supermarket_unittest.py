import unittest

from model_objects import Product, SpecialOfferType, ProductUnit
from shopping_cart import ShoppingCart
from teller import Teller
from fake_catalog import FakeCatalog

class TestTennis(unittest.TestCase):

    def test_ten_percent_discount(self):
        catalog = FakeCatalog()
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        catalog.add_product(toothbrush, 0.99)

        apples = Product("apples", ProductUnit.KILO)
        catalog.add_product(apples, 1.99)

        teller = Teller(catalog)
        teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

        cart = ShoppingCart()
        cart.add_item_quantity(apples, 2.5)

        receipt = teller.checks_out_articles_from(cart)

        self.assertEqual([], receipt.discounts)
        self.assertEqual(1, len(receipt.items))
        receipt_item = receipt.items[0]
        self.assertEqual(apples, receipt_item.product)
        self.assertEqual(1.99, receipt_item.price)
        self.assertEqual(2.5, receipt_item.quantity)
        self.assertAlmostEqual(4.975, receipt.total_price(), 0.01)
        self.assertAlmostEqual(2.5 * 1.99, receipt.total_price(), 0.01)


if __name__ == "__main__":
    unittest.main()