from django.test import SimpleTestCase
from . import ethereum_utils


# Create your tests here.

class EthereumUtilsTestCase(SimpleTestCase):

    def setUp(self):
        pass

    def test_get_keystore(self):
        keystore = ethereum_utils.getKeystore()
        self.assertIsNotNone(keystore)
