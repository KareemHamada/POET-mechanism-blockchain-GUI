from dataclasses import dataclass
from random import randint

@dataclass
class Inventory_management:
    def __init__(self,network):
        self.network = network
        self.products = []
        self.categories = []
        self.product()
        self.management()
        
        
    def product(self):
        print("####################################################################")
        print("############### Hello in our Inventory management app\n  ##########")
        print("##################################################################")
        print("\n")
        print("\n")
        print("####################  It is time to enter categories    ###########")
        while True:
            category = input("Enter the product category : ")
            self.categories.append(category)
            contin = input("Do you want to enter more categories?(y/n): ")
            if contin.lower() == 'y':
                continue
            else:
                break
        
        print("####################################################################")
        print("#####################     It is time to enter products  ############")
        print("####################################################################")
        while True:
            
            name = input("Enter the product name : ")
            category = input(f"Enter the product category {self.categories} : ")
            self.products.append([name,category])

            contin = input("Do you want to enter more products?(y/n): ")
            if contin.lower() == 'y':
                continue
            else:
                break
        return True

    def management(self):
        """
            get the products of the same category and add them to the block
        """

        container = []
        candidates_list = []
        # list of product of same category
        products_of_same_category = []

        for category in self.categories:
            for product in self.products:
                if product[1] == category:
                    products_of_same_category.append(product)
            
            container.append(products_of_same_category)
            products_of_same_category = []


        x = 1
        for node,same_category in zip(self.network,container):
            winner,selected_time,elapsed_time,candidates = node.blockchain.proof(self.network, [randint(1, 20) for _ in self.network])
            node.blockchain.add_block(same_category, winner)
            
            for candidate in candidates:
                candidates_list.append(candidate.name)
             
            print(f"####################    Info about {x} Block   ###############")
            print(f"""
                    'Winner Name' : {winner.name}\n
                    'Candidates' : {candidates_list}\n
                    'Random Times ': {elapsed_time}\n
                    'Selected Time' : {selected_time}\n
                """)
            x+= 1

        winner.blockchain.print()