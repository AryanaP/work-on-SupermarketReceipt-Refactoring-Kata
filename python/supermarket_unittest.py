import unittest

from model_objects import Product, SpecialOfferType, ProductUnit, Discount, Offer
from shopping_cart import ShoppingCart
from teller import Teller
from fake_catalog import FakeCatalog
from receipt import Receipt, ReceiptItem

class TestTennis(unittest.TestCase):

# CATALOG.PY
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

# RECEIPT.PY
    def test_receipt_total_price(self):
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        apples = Product("apples", ProductUnit.KILO)
        toothbrush_discount = Discount(toothbrush, "my_description", 0.2)
        receipt_toothbrush = ReceiptItem(toothbrush, 2, 1.5, 3)
        receipt_apples = ReceiptItem(apples, 3, 1, 3)

        receipt = Receipt()
        receipt.discounts = [toothbrush_discount]
        receipt.items = [receipt_toothbrush, receipt_apples]
        totalprice = receipt.total_price()

        self.assertEqual([toothbrush_discount], receipt.discounts)
        self.assertEqual(5.8, totalprice)

    def test_receipt_add_product(self):
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        apples = Product("apples", ProductUnit.KILO)
        receipt_toothbrush = ReceiptItem(toothbrush, 2, 1.5, 3)

        receipt = Receipt()
        receipt.discount = []
        receipt._items = [receipt_toothbrush]
        self.assertEqual(1, len(receipt._items))

        receipt.add_product(apples, 2, 1, 2)
        self.assertEqual(2, len(receipt._items))

    def test_receipt_add_discount(self):
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        receipt_toothbrush = ReceiptItem(toothbrush, 2, 1.5, 3)

        discount = Discount(toothbrush, "test", 1.5)

        receipt = Receipt()
        receipt._items = [receipt_toothbrush]
        self.assertEqual(0, len(receipt._discounts))

        receipt.add_discount(discount)
        self.assertEqual(1, len(receipt._discounts))
        self.assertEqual(discount, receipt._discounts[0])

# SHOPPING_CART.PY
    def test_shopping_cart_add_item(self):
        cart = ShoppingCart()
        apples = Product("apples", ProductUnit.KILO)

        self.assertEqual(0, len(cart._items))
        cart.add_item(apples)
        self.assertEqual(1, len(cart._items))

    def test_shopping_cart_add_item_quantity(self):
        cart = ShoppingCart()
        apples = Product("apples", ProductUnit.KILO)

        cart.add_item_quantity(apples, 2.5)
        self.assertEqual(2.5, cart.product_quantities[apples])

        cart.add_item_quantity(apples, 1.2)
        self.assertEqual(3.7, cart.product_quantities[apples])

    def test_shopping_handle_offers_no_offers(self):
        catalog = FakeCatalog()
        toothbrush = Product("toothbrush", ProductUnit.EACH)
        receipt_toothbrush = ReceiptItem(toothbrush, 2, 1.5, 3)

        receipt = Receipt()
        receipt.items = [receipt_toothbrush]

        receipt_offers = {}

        cart = ShoppingCart()
        cart._items = [toothbrush]
        cart._product_quantities = {toothbrush: 2}

        cart.handle_offers(receipt, receipt_offers, catalog)
        self.assertEqual([], receipt.discounts)

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
        #cart.add_item_quantity(toothbrush, 2)

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
