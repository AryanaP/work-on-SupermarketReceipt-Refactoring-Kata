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

        self.assertEqual({"apples":apples, "toothbrush":toothbrush}, catalog.products)

    def test_catalog_unit_price(self):
        catalog = FakeCatalog()
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        apples = Product("apples", ProductUnit.KILO)

        catalog.add_product(toothbrush, 0.99)
        catalog.add_product(apples, 1.99)

        self.assertEqual(0.99, catalog.unit_price(toothbrush))
        self.assertEqual(1.99, catalog.unit_price(apples))

    def test_shopping_cart_add_item_quantity(self):
        cart = ShoppingCart()
        apples = Product("apples", ProductUnit.KILO)

        cart.add_item_quantity(apples, 2.5)
        self.assertEqual(2.5, cart.product_quantities[apples])

        cart.add_item_quantity(apples, 1.2)
        self.assertEqual(3.7, cart.product_quantities[apples])

   # def test_shopping_cart_handle_offers(self):


    #def test_shopping_cart_handle_offers_three_for_two(self):
    #    catalog = FakeCatalog()
    #    toothbrush = Product("toothbrush", ProductUnit.EACH)
    #    apples = Product("apples", ProductUnit.KILO)
    #    catalog.add_product(toothbrush, 0.99)
    #    catalog.add_product(apples, 1.99)

        # teller special offers 3 for 2 discount on toothbrush
    #    teller = Teller(catalog)
    #    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 0)

        # add apples to shopping cart
#        cart = ShoppingCart()
#        cart.add_item_quantity(apples, 2.5)

#        receipt = teller.checks_out_articles_from(cart)

        # add apples to shopping cart : check no discounts and 1 item
#        self.assertEqual([], receipt.discounts)
#        self.assertEqual(len(cart.items), len(receipt.items))
#        receipt_item = receipt.items[0]
#        self.assertEqual(apples, receipt_item.product)
#        self.assertEqual(catalog.unit_price(apples), receipt_item.price)
#        self.assertEqual(cart.product_quantities[apples], receipt_item.quantity)
#        self.assertAlmostEqual(cart.product_quantities[apples] * catalog.unit_price(apples), receipt.total_price(), 0.01)


    def test_shopping_cart_handle_offers_ten_percent_discount(self):
        catalog = FakeCatalog()
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        apples = Product("apples", ProductUnit.KILO)
        catalog.add_product(toothbrush, 0.99)
        catalog.add_product(apples, 1.99)

        # teller special offers 10% discount on toothbrush
        teller = Teller(catalog)
        teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)
        #offers = teller.offers
        #discount = Discount(product, "2 for " + str(offer.argument), discount_n)

        # add apples to shopping cart
        cart = ShoppingCart()
        cart.add_item_quantity(apples, 2.5)
        cart.add_item_quantity(toothbrush, 2)

        receipt = teller.checks_out_articles_from(cart)

        # add apples to shopping cart : check no discounts and 1 item
        #self.assertEqual([], receipt.discounts)
        #self.assertEqual(len(cart.items), len(receipt.items))
        #receipt_item = receipt.items[0]
        #self.assertEqual(apples, receipt_item.product)
        #self.assertEqual(catalog.unit_price(apples), receipt_item.price)
        #self.assertEqual(cart.product_quantities[apples], receipt_item.quantity)
        #self.assertAlmostEqual(cart.product_quantities[apples] * catalog.unit_price(apples), receipt.total_price(), 0.01)

if __name__ == "__main__":
    unittest.main()
