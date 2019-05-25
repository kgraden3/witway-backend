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

    def test_estimate_gas_cost(self):
        transaction = self.utils.create_transaction("0x93F916f1cc5F074BfF9E63c4dB7c0DdBEBD8C263", 1)
        self.utils.get_gas_estimate(transaction)
