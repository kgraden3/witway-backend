from web3 import Web3
import os
from django.conf import settings


class EthereumUtils:

    def __init__(self):
        provider = Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/feb06b6a31854be7b91a77f307fc94cc')
        self.w3 = Web3(provider)
        self.addr = '0x5b7bd33cfa8f37951e78d5a52436c2e65a8b0d83'
        self.checksum_addr = self.w3.toChecksumAddress('0x5b7bd33cfa8f37951e78d5a52436c2e65a8b0d83')
        self.private_key = self.decrypt_keystore()

    def get_keystore(self):
        return open(os.path.join(settings.BASE_DIR, 'witway-keystore')).read()

    def decrypt_keystore(self):
        keystore = self.get_keystore()
        private_key = self.w3.eth.account.decrypt(keystore, settings.WITWAY_ADDRESS_SECRET)
        return private_key

    def get_gas_estimate(self, transaction):
        return self.w3.eth.estimateGas(transaction)

    def get_gas_price(self):
        return self.w3.eth.gasPrice

    def get_nonce(self):
        return self.w3.eth.getTransactionCount(self.checksum_addr)

    def get_account(self):
        return self.account

    def create_unsigned_transaction(self, to, value, nonce, gas_price=None, gas=None):
        transaction = {
            'to': self.w3.toChecksumAddress(to),
            'from': self.checksum_addr,
            'value': value,
            'nonce': nonce
        }

        if gas_price:
            transaction['gasPrice'] = gas_price

        if gas:
            transaction['gas'] = gas

        return transaction

    def get_signed_transaction(self, transaction):
        return self.w3.eth.account.signTransaction(transaction, self.private_key)

    def send_raw_transaction(self, raw_transaction):
        return self.w3.eth.sendRawTransaction(raw_transaction)
