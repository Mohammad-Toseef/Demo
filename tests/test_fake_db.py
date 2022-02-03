"""Script to create Fake database and a fake test table inside it for testing CRUD operations """

from unittest import TestCase
from unittest.mock import patch
import sys
sys.path.append("../crud-app")
import os
import mysql.connector
from mysql.connector import errorcode
from crud-app.src.csv_db_package.crud_operations import config as crud_operations_config


os.environ['HOST'] = 'localhost'
os.environ['USER'] = 'root'
os.environ['PASSWORD'] = 'Arp@99?0#1Liy@'


MYSQL_USER = os.getenv("USER")
MYSQL_PASSWORD = os.getenv('PASSWORD')
MYSQL_DB = "testdb"
MYSQL_HOST = os.getenv('HOST')


# MYSQL_PORT = "3306"


class MockDB(TestCase):
    """
        class contains setup class method and teardown class method
        for creating and deleting the db respectively.
    """
    @classmethod
    def setUpClass(cls):
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        cursor = conn.cursor(dictionary=True)

        # drop database if it already exists
        try:
            cursor.execute(f"DROP DATABASE {MYSQL_DB}")
            cursor.close()
            print("DB dropped")
        except mysql.connector.Error as err:
            print(f"{MYSQL_DB}{err}")

        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                f"CREATE DATABASE {MYSQL_DB} DEFAULT CHARACTER SET 'utf8'")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")
            sys.exit(1)
        conn.database = MYSQL_DB

        query = """
                        CREATE TABLE test_table(p_id int PRIMARY KEY, first_name varchar(255),height_feet float,
                        height_inches float, last_name varchar(255),position varchar(255),weight_pounds float,id int,
                        abbreviation varchar(255),city varchar(255), conference varchar(255), division varchar(255),
                        full_name varchar(255), name varchar(255))
                     """
        try:
            cursor.execute(query)
            conn.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
        cursor.close()
        conn.close()

        testconfig = {
            'host': MYSQL_HOST,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD,
            'database': MYSQL_DB
        }
        cls.mock_db_config = patch.dict(crud_operations_config, testconfig)

    @classmethod
    def tearDownClass(cls):
        cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute(f"DROP DATABASE {MYSQL_DB}")
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Database {MYSQL_DB} does not exists. Dropping db failed {err}")
        cnx.close()
