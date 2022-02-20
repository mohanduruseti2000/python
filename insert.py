import mysql.connector
import time
from mysql.connector import errorcode
import logging

logging.basicConfig(level=logging.INFO)
class Demo:
    def __init__(self, dtatbase):
        self.database = database
                                      """It is creating the table"""
    def create_table(self):
        db_connection = None
        try:
            db_connection = mysql.connector.connect(user='Dhoni', password='dhoni07', host='127.0.0.1', database=self.database)
            logging.info("connection established successfully......")
            my_cursor = db_connection.cursor()
            time.sleep(.4)
            t_name = input("Enter the table name to be created: ")
            s_no = input("Enter the name of 1st column: ")
            s_no_type = input("Datatype: ")
            s_name = input("Enter the 2nd column name: ")
            s_name_type = input("Datatype: ")
            s_age = input("Enter the 3rd column name: ")
            s_age_type = input("Datatype: ")
            marks = input("Enter the 4th column name: ")
            marks_type = input("Datatype: ")
            query = f'CREATE TABLE {t_name} ({s_no} {s_no_type}, {s_name} {s_name_type}, {s_age} {s_age_type}, {marks} {marks_type})'
            my_cursor.execute(query)
            db_connection.commit()
            logging.info("........Table created successfully..........")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DEFINED_ERROR:
                logging.warning("something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
               db_connection.close()

                             """It is for inserting a row"""
    def insert_data_to_table(self):
        db_connection = None
        try:
            db_connection = mysql.connector.connect(user='Dhoni',password='dhoni07',host='127.0.0.1',database=self.database)
            logging.info("........connection established successfully......")
            my_cursor = db_connection.cursor()
            time.sleep(0.4)
            t_name = input("Enter the table name in which you want to insert: ")
            print("plz insert those details to add it to the table: ")
            s_id = input("Enter the id of "+t_name+": ")
            s_name = input("Enter the name of " +t_name+": ")
            s_age = input("Enter the age " +t_name+": ")
            marks = input("Enter the marks " +t_name+": ")
            query = f'INSERT INTO {t_name} values(%s, %s, %s, %s)'
            val = (s_id, s_name, s_age, marks)
            my_cursor.execute(query, val)
            db_connection.commit()
            db_connection.close()
            logging.info("...........Data inserted successfully...........")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("something is wrong with your username or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()


                              """Its for deleting code"""
    def delete_from_table(self):
        db_connection = None
        try:
            db_connection = mysql.connector.connect(user='Dhoni',password='dhoni07',host='127.0.0.1',database=self.database)
            logging.info("........connection established successfully........")
            my_cursor = db_connection.cursor()
            time.sleep(0.4)
            t_name = input("Enter the table name to delete the data:")
            s_id = int(input("Enter the id of the"+t_name+" which u want to delete:"))
            query = f'DELETE FROM {t_name} values(%s)'
            val = (s_id)
            my_cursor.execute(query, val)
            db_connection.commit()
            db_connection.close()
            logging.info(".........Data Deleted successfully.........")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("something is went wrong in your username or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()

                                  """Its for update code"""
    def update_table_data(self):
        db_connection = None
        try:
            db_connection = mysql.connector.connect(user='Dhoni', password='dhoni07', host='127.0.0.1',
                                                    database=self.database)
            logging.info("Connection Established Successfully!")
            my_cursor = db_connection.cursor()
            time.sleep(0.5)
            t_name = input("Enter the table name to update table data : ")
            print("Enter details to Update table data : ")
            id = int(input("Enter the " + t_name + " proper Id : "))
            val = input("Enter the value which you want to update : ")
            column_name = input("Enter the column name whose data you want to update : ")
            query = f'UPDATE {t_name} set {column_name} = "{val}" WHERE ID={id}'
            my_cursor.execute(query)
            db_connection.commit()
            db_connection.close()
            logging.info("Data updated Successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()

                                   """its code for drop the commend"""
    def drop_a_table(self):
        db_connection = None
        try:
            db_connection = mysql.connector.connect(user='Dhoni', password='dhoni07', host='127.0.0.1',database=self.database)
            logging.info(".....Connection Established Successfully!........")
            my_cursor = db_connection.cursor()
            time.sleep(0.5)
            t_name = input("Enter the table name drop : ")
            query = f'DROP TABLE {t_name}'
            my_cursor.execute(query)
            db_connection.commit()
            db_connection.close()
            logging.info("Table Dropped Successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()




database = input("Enter your databse name : ")
while True:
    d = Demo(database)
    user_choice = int(input('''Enter your choice :
    1.CREATE TABLE
    2.INSERT DATA
    3.DELETE FROM TABLE
    4.UPDATE TABLE DATA
    5.DROP A TABLE \n'''))

    if user_choice == 1:
        d.create_table()
    elif user_choice == 2:
        d.insert_data_to_table()
    elif user_choice == 3:
        d.delete_from_table()
    elif user_choice == 4:
        d.update_table_data()
    elif user_choice == 5:
        d.drop_a_table()
    else:
        logging.warning("INVALID INPUT......")
    time.sleep(0.5)
    choice = input("Do you want to continue (y/n) : ")
    if choice == 'y' or choice == 'Y':
        continue
    else:
        break

