import os
import logging
from mysql.connector import connect, errors


MYSQL_USER = os.getenv("USER")
MYSQL_PASSWORD = os.getenv('PASSWORD')
MYSQL_DB = "user_data"
MYSQL_HOST = os.getenv('HOST')


def create_table():
    create_table_query = """
                            CREATE TABLE user_file_data(p_id int PRIMARY KEY, first_name varchar(255),height_feet float,
                            height_inches float, last_name varchar(255),position varchar(255),weight_pounds float,id int,
                            abbreviation varchar(255),city varchar(255), conference varchar(255), division varchar(255),
                            full_name varchar(255), name varchar(255))
                         """
    try:
        conn = connect(host=MYSQL_HOST,
                       database=MYSQL_DB,
                       user=MYSQL_USER,
                       password=MYSQL_PASSWORD)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            logging.info("You're connected to database: %s", record)
            cursor.execute('DROP TABLE IF EXISTS user_file_data;')
            logging.info('Creating table....')

            cursor.execute(create_table_query)
            logging.info("Table is created....")
        return "Table created successfully"
    except errors.ProgrammingError as prmg_err:
        logging.error('%s: %s', prmg_err.__class__.__name__, prmg_err)
    except errors.Error as err_e:
        logging.error('%s: %s', err_e.__class__.__name__, err_e)
