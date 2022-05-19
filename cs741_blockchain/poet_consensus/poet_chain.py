from cs741_blockchain.interface.chain import Blockchain
from random import randint

class POET_Blockchain(Blockchain):
    def proof(self, candidates, elapsed_time):
        # minimum time for selected node
        selected_time = min(elapsed_time)
        winner = None

        # candidate with minimum time == winner
        for candidate , time in zip(candidates, elapsed_time):
            if time == selected_time:
                winner = candidate
                break
        return winner,selected_time,elapsed_time,candidates