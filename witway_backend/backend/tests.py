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
