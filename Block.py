import hashlib
import json
from time import time


class Blockchain(object):

    def __init__(self):

        self.chain = []
        self.pending_transactions = []

        self.new_block(
            previous_hash="I am hash of previous Block.", proof_of_work=100)

    def new_block(self, proof_of_work, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof_of_work': previous_hash or self.hash(self.chain[-1]),
        }

        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain = Blockchain()

first_transaction = blockchain.new_transaction("Babu", "Manoj", '5 BTC')

second_transaction = blockchain.new_transaction(
    "Manoj", "Shubankar Das", '1 BTC')

third_transaction = blockchain.new_transaction(
    "Shubankar Das", "Albin Benny", '5 BTC')

blockchain.new_block(12345)

fourth_transaction = blockchain.new_transaction(
    "Albin Benny", "Shaastri", '1 BTC')

fifth_transaction = blockchain.new_transaction("Shaastri", "Babu", '0.5 BTC')

Sixth_transaction = blockchain.new_transaction("Babu", "Manoj", '2 BTC')

blockchain.new_block(678910)

print("***********Welcome to My Blockchain in Python Programming**********", blockchain.chain)
