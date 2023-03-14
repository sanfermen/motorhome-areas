import pandas as pd
import mysql.connector

class Database_SQL:
    def __init__(self, name_bbdd, password):
        """
        This class is used to connect to a database and execute SQL queries
            Parameters:
                database name and password
        """ 
        self.name_bbdd = name_bbdd
        self.password = password
    
    def create_bbdd(self):
        """
        Creating a database. If we can't execute the query, we print the error
        """
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password= f'{self.password}' 
        )
        print("Connection successful")
        
        mycursor = mydb.cursor()

        try:
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.name_bbdd};")
            print(mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)


    def create_tabla(self, query):
        """
        We connect to the database using the connector, we create a cursor, and we try to execute the
        query. If we can't execute the query, we print the error
        
        Param query: The query you want to execute
        """
    
        cnx = mysql.connector.connect(user='root', password=f"{self.password}",
                                        host='127.0.0.1', database=f"{self.name_bbdd}")
    
        mycursor = cnx.cursor()
       
        try: 
            mycursor.execute(query)
            cnx.commit() 
        
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)


    def insert_data(self, query):
        """
        It connects to the database, creates a cursor, and then executes the query. 
        If the query is successful, it commits the changes to the database. 
        If the query fails, it prints the error message.
        
        Param query: The query you want to execute
        """
        cnx = mysql.connector.connect(user='root', password=f"{self.password}",
                                    host='127.0.0.1', database=f"{self.name_bbdd}")
        mycursor = cnx.cursor()
        
        try: 
            # Disabling the foreign key checks. 
            # This is because we want to insert data into the database
            mycursor.execute("SET foreign_key_checks = 0;")
            mycursor.execute(query)
            cnx.commit()
            mycursor.execute("SET foreign_key_checks = 1;")

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
        