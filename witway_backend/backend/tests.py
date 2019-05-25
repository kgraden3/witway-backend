from django.test import SimpleTestCase
from .ethereum_utils import EthereumUtils


# Create your tests here.

class EthereumUtilsTestCase(SimpleTestCase):

    def setUp(self):
        self.utils = EthereumUtils()
        self.TEST_ACCOUNT = "0xa2e1d85c8ac2dff1c91a862552dbc4da6fa4d8b2"

        pass

    def test_get_keystore(self):
        keystore = self.utils.get_keystore()
        self.assertIsNotNone(keystore)

    def test_decrypt_keystore(self):
        private_key = self.utils.decrypt_keystore()
        print(private_key)

    def test_is_connected(self):
        self.assertTrue(self.utils.w3.isConnected())

    def test_nonce(self):
        nonce = self.utils.get_nonce()
        print(nonce)
        self.assertIsNotNone(nonce)

    def test_estimate_gas(self):
        nonce = self.utils.get_nonce()
        transaction = self.utils.create_unsigned_transaction(self.TEST_ACCOUNT, 1, nonce)
        estimate = self.utils.get_gas_estimate(transaction)
        print(estimate)
        self.assertIsNotNone(estimate)

    def test_gas_price(self):
        price = self.utils.get_gas_price()
        print(price)
        self.assertIsNotNone(price)

    def test_signed_transaction(self):
        nonce = self.utils.get_nonce()
        transaction = self.utils.create_unsigned_transaction(self.TEST_ACCOUNT, 1, nonce)
        gas_price = self.utils.get_gas_price()
        gas = self.utils.get_gas_estimate(transaction)
        transaction = self.utils.create_unsigned_transaction(self.TEST_ACCOUNT, 1, nonce, gas_price, gas)
        signed = self.utils.get_signed_transaction(transaction)
        print(signed)
        self.assertIsNotNone(signed)
