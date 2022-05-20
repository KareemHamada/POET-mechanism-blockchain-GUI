import pyodbc

conn = pyodbc.connect(
    "Driver={SQL SERVER};"
    "Server=DESKTOP-ADO823G;"
    "Database=poet;"
    "Trusted_connection=yes;"
)