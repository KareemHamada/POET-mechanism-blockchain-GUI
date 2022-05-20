from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from datetime import datetime
from random import randint
import time
from typing import List
from cs741_blockchain import Node
from cs741_blockchain.poet_consensus.poet_chain import POET_Blockchain
from cs741_blockchain.poet_consensus.Inventory_management import Inventory_management
from sql import conn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 778)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(150, 30, 880, 50))
        self.header_label.setMinimumSize(QtCore.QSize(0, 50))
        self.header_label.setStyleSheet("font-size:25px;")
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.message_viewer = QtWidgets.QTextBrowser(self.centralwidget)
        self.message_viewer.setGeometry(QtCore.QRect(455, 100, 700, 611))
        self.message_viewer.setStyleSheet("font-size:15px;\n"
"color: rgb(0, 85, 0);\n"
"")
        self.message_viewer.setObjectName("message_viewer")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 101, 441, 171))
        self.listView.setStyleSheet("")
        self.listView.setObjectName("listView")
        self.category = QtWidgets.QLineEdit(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(20, 140, 391, 31))
        self.category.setMinimumSize(QtCore.QSize(0, 0))
        self.category.setAlignment(QtCore.Qt.AlignCenter)
        self.category.setObjectName("category")
        self.add_category = QtWidgets.QPushButton(self.centralwidget)
        self.add_category.setGeometry(QtCore.QRect(30, 210, 371, 25))
        self.add_category.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 85, 0,0.2);\n"
"border:1px solid  rgb(0, 85, 0);\n"
"border-radius:6px;\n"
"width:80px;\n"
"height:23px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 85, 0,0.1);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 85, 0,0.2);\n"
"}")
        self.add_category.setObjectName("add_category")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(10, 301, 441, 221))
        self.listView_2.setStyleSheet("")
        self.listView_2.setObjectName("listView_2")
        self.add_product = QtWidgets.QPushButton(self.centralwidget)
        self.add_product.setGeometry(QtCore.QRect(30, 470, 371, 25))
        self.add_product.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 85, 0,0.2);\n"
"border:1px solid  rgb(0, 85, 0);\n"
"border-radius:6px;\n"
"width:80px;\n"
"height:23px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 85, 0,0.1);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 85, 0,0.2);\n"
"}")
        self.add_product.setObjectName("add_product")
        self.product_name = QtWidgets.QLineEdit(self.centralwidget)
        self.product_name.setGeometry(QtCore.QRect(20, 340, 391, 31))
        self.product_name.setMinimumSize(QtCore.QSize(0, 0))
        self.product_name.setAlignment(QtCore.Qt.AlignCenter)
        self.product_name.setObjectName("product_name")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 390, 391, 31))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.request_to_mine = QtWidgets.QPushButton(self.centralwidget)
        self.request_to_mine.setGeometry(QtCore.QRect(30, 610, 371, 25))
        self.request_to_mine.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 85, 0,0.2);\n"
"border:1px solid  rgb(0, 85, 0);\n"
"border-radius:6px;\n"
"width:80px;\n"
"height:23px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 85, 0,0.1);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 85, 0,0.2);\n"
"}")
        self.request_to_mine.setObjectName("request_to_mine")
        self.delete_all_products = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all_products.setGeometry(QtCore.QRect(30, 650, 371, 25))
        self.delete_all_products.setStyleSheet("QPushButton{\n"
"border:1px solid #b01e0b;\n"
"border-radius:6px;\n"
"background-color: rgba(176, 30, 11, 0.2);\n"
"width:80px;\n"
"height:23px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(176, 30, 11, 0.1);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(176, 30, 11, 0.2);\n"
"}\n"
"")
        self.delete_all_products.setObjectName("delete_all_products")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tik()
        self.tok()
        self.actions()

        cursor = conn.cursor()
        cursor.execute("select * from category")
        for row in cursor:
            self.comboBox.addItem(row[1])
            
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def actions(self):
        self.add_category.clicked.connect(self.add_category_func)
        self.add_product.clicked.connect(self.add_product_func)
        self.delete_all_products.clicked.connect(self.delete_all_products_func)
        self.request_to_mine.clicked.connect(self.mine)
        
    def add_category_func(self):
        category_name = self.category.text()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO category (name) VALUES (?)", (category_name))
        conn.commit()
        self.comboBox.addItem(category_name)
        # cursor.execute("select * from category")
        # for row in cursor:
        #     self.comboBox.addItem(row[1])
        self.category.clear()

    def add_product_func(self):
        product_name = self.product_name.text()  
        category_name = self.comboBox.currentText()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product (name,category) VALUES (?,?)", (product_name, category_name))
        conn.commit()
        self.product_name.clear()

    def delete_all_products_func(self):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM product")
        conn.commit()
        self.message_viewer.clear()

    # def main(self):
    #     Inventory_management(network)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header_label.setText(_translate("MainWindow", "Inventory Management App"))
        self.message_viewer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.category.setPlaceholderText(_translate("MainWindow", "Category"))
        self.add_category.setText(_translate("MainWindow", "Add Category"))
        self.add_product.setText(_translate("MainWindow", "Add Product"))
        self.product_name.setPlaceholderText(_translate("MainWindow", "Product Name"))
        self.request_to_mine.setText(_translate("MainWindow", "Request to mine"))
        self.delete_all_products.setText(_translate("MainWindow", "Delete all products"))

    def mine(self):
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

        obj = Inventory_management(network)
        owner,winner_list,candidates_list,elapsed_time_list,selected_time_list  = obj.management()
        #self.message_viewer.setText(winner.name)
        self.message_viewer.append("Analysis Prove")
        x = 1
        for winner,elapsed_time,selected_time in zip(winner_list,elapsed_time_list,selected_time_list):
            self.message_viewer.append(f"Info about {x} Block")
            self.message_viewer.append(f"\t Winner : {winner}")
            self.message_viewer.append(f"\t Candidates list : {candidates_list}")
            self.message_viewer.append(f"\t Random time : {elapsed_time}")
            self.message_viewer.append(f"\t Selected time : {selected_time}")
            x+=1
            self.message_viewer.append("")

        self.message_viewer.append("")
        self.message_viewer.append("")
        chain = owner.blockchain.chain
        self.message_viewer.append("Blockchain:\n")
        self.message_viewer.append(f"\tOwned by: {owner.name}")
        self.message_viewer.append(f"\tchain: [")
        for block in chain:
            self.message_viewer.append("\t\tBlock:")
            self.message_viewer.append(f"\t\t\tcreation_time: {block.creation_time}")
            self.message_viewer.append(f"\t\t\tcreated_by: {block.create_by.name}")
            self.message_viewer.append(f"\t\t\tprev_hash: {block.prev_hash[:6]}")
            self.message_viewer.append(f"\t\t\thash: {block.hash[:6]}")
            self.message_viewer.append(f"\t\t\ttransactions: [")
            for transaction in block.transactions:
                self.message_viewer.append("\t\t\t\tTransaction:")
                self.message_viewer.append(f"\t\t\t\t\thash: {transaction.hash[:6]}")
                self.message_viewer.append(f"\t\t\t\t\tprev_hash: {transaction.prev_hash[:6]}")
                self.message_viewer.append(f"\t\t\t\t\tdata: {transaction.data}")
            self.message_viewer.append(f"\t\t\t]")
            self.message_viewer.append(f"\t\t\tseal_time: {block.seal_time}")
        self.message_viewer.append((f"\t]"))
        



    def tik(self):
        global start_time
        start_time = time.time()

    def tok(self):
        global start_time
        time_interval = round(time.time() - start_time, 2)
        print("\nTook", time_interval, "seconds.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
