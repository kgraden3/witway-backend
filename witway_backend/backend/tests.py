from django.test import SimpleTestCase
from .ethereum_utils import EthereumUtils


# Create your tests here.

class EthereumUtilsTestCase(SimpleTestCase):

    def setUp(self):
        self.utils = EthereumUtils()

        pass

    def test_get_keystore(self):
        keystore = self.utils.get_keystore()
        self.assertIsNotNone(keystore)

    def test_decrypt_keystore(self):
        private_key = self.utils.decrypt_keystore()
        print(private_key)

    def test_is_connected(self):
        self.assertTrue(self.utils.w3.isConnected())

    def test_estimate_gas(self):
        transaction = self.utils.create_unsigned_transaction("0xa2e1d85c8ac2dff1c91a862552dbc4da6fa4d8b2", 1)
        estimate = self.utils.get_gas_estimate(transaction)
        print(estimate)
        self.assertIsNotNone(estimate)

    def test_gas_price(self):
        price = self.utils.get_gas_price()
        print(price)
        self.assertIsNotNone(price)

