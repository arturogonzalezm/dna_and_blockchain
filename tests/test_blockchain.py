import time
from backend.simple_blockchain.blockchain import Blockchain, Block


def test_create_genesis_block():
    blockchain = Blockchain()
    genesis_block = blockchain.chain[0]
    assert genesis_block.index == 0
    assert genesis_block.data == "Genesis Block"
    assert genesis_block.previous_hash == "0"


def test_add_block():
    blockchain = Blockchain()
    initial_chain_length = len(blockchain.chain)
    new_block = Block(1, time.time(), {"data": "New Block"}, blockchain.get_latest_block().hash)
    blockchain.add_block(new_block)
    assert len(blockchain.chain) == initial_chain_length + 1
    assert blockchain.chain[-1].data == {"data": "New Block"}


def test_is_chain_valid():
    blockchain = Blockchain()
    new_block = Block(1, time.time(), {"data": "New Block"}, blockchain.get_latest_block().hash)
    blockchain.add_block(new_block)
    assert blockchain.is_chain_valid()

    # Tampering with the data
    blockchain.chain[1].data = {"data": "Tampered Block"}
    assert not blockchain.is_chain_valid()
