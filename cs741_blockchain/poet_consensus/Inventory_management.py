from dataclasses import dataclass
from random import randint
from sql import conn

@dataclass
class Inventory_management:
    def __init__(self,network):
        self.network = network
        # self.products = []
        # self.categories = []
        #self.management()
        

    def management(self):
        """
            get the products of the same category and add them to the block
        """

        container = []
        
        # list of product of same category
        products_of_same_category = []
        cursor = conn.cursor()
        categories = cursor.execute("select * from category").fetchall()
        products = cursor.execute("select * from product").fetchall()
        categories_list = [category[1] for category in categories]
        products_list = [[product[1],product[2]] for product in products]
        # print(categories_list)
        # print(products_list)
        for category in categories_list:
            for product in products_list:
                if product[1] == category:
                    products_of_same_category.append(product)
            
            container.append(products_of_same_category)
            products_of_same_category = []


        # x = 1
        winner_list = []
        candidates_list = []
        elapsed_time_list = []
        selected_time_list = []

        for node,same_category in zip(self.network,container):
            winner,selected_time,elapsed_time,candidates = node.blockchain.proof(self.network, [randint(1, 20) for _ in self.network])
            node.blockchain.add_block(same_category, winner)
            
            # for candidate in candidates:
            #     candidates_list.append(candidate.name)
            
            winner_list.append(winner.name)
            elapsed_time_list.append(elapsed_time)
            selected_time_list.append(selected_time)
            
            # print(f"####################    Info about {x} Block   ###############")
            # print(f"""
            #         'Winner Name' : {winner.name}\n
            #         'Candidates' : {candidates_list}\n
            #         'Random Times ': {elapsed_time}\n
            #         'Selected Time' : {selected_time}\n
            #     """)
            # candidates_list = []
            # x+= 1
        
        for candidate in candidates:
            candidates_list.append(candidate.name)
        return winner,winner_list,candidates_list,elapsed_time_list,selected_time_list 
        #winner.blockchain.print()