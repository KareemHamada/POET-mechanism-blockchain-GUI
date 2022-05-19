
from datetime import datetime
from random import randint
import time
from typing import List
from cs741_blockchain import Node
from cs741_blockchain.poet_consensus.poet_chain import POET_Blockchain
from cs741_blockchain.poet_consensus.Inventory_management import Inventory_management


def main():
    # Creating network of nodes
    network: List[Node] = []
    kareem_node = Node('Kareem', '0.0.0.1', 70, network)
    rowida_node = Node('Rowida', '0.0.0.2', 100, network)
    abdalla_node = Node('Abdalla', '0.0.0.3', 50, network)
    fatma_node = Node('Fatma', '0.0.0.4', 30, network)

    network.append(kareem_node)
    network.append(rowida_node)
    network.append(abdalla_node)
    network.append(fatma_node)

    kareem_node.blockchain = POET_Blockchain(kareem_node)
    rowida_node.blockchain = POET_Blockchain(rowida_node)
    abdalla_node.blockchain = POET_Blockchain(abdalla_node)
    fatma_node.blockchain = POET_Blockchain(fatma_node)

    Inventory_management(network)

def tik():
    global start_time
    start_time = time.time()

def tok():
    global start_time
    time_interval = round(time.time() - start_time, 2)
    print("\nTook", time_interval, "seconds.")


if __name__ == '__main__':
    tik()
    main()
    tok()
