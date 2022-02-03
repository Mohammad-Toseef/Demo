"""Script performs various test for CRUD operations in database"""

import os
import sys
sys.path.append("../crud-app")
from mysql.connector.errors import IntegrityError, ProgrammingError, DatabaseError
from test_fake_db import MockDB, MYSQL_DB
import test_rows as rw
from crud-app.src.csv_db_package.crud_operations import insert_row, delete_row, update_row, view_data

os.environ['HOST'] = 'localhost'
os.environ['USER'] = 'root'
os.environ['PASSWORD'] = 'Arp@99?0#1Liy@'


class TestCrudData(MockDB):
    """Test class for testing the different operations on database
        went successful or not by defining different methods"""
    def test_1_insert_in_database_successful(self):
        """Checks if data inserted into database table is successfully inserted"""
        with self.mock_db_config:
            self.assertEqual(insert_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_1), "Successfully Inserted")
            self.assertEqual(insert_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_2), "Successfully Inserted")
            self.assertEqual(insert_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_3), "Successfully Inserted")
            self.assertEqual(insert_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_4), "Successfully Inserted")
            self.assertEqual(insert_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_6), "Successfully Inserted")
            self.assertEqual(insert_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_9), "Successfully Inserted")
            self.assertEqual(insert_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_0), "Successfully Inserted")

    def test_2_insert_in_db_unsuccessful(self):
        """Checks if inserting wrong values throws exception"""
        with self.mock_db_config:
            with self.assertRaises(IntegrityError):
                insert_row(db_name=MYSQL_DB, db_table='test_table', dict_values=rw.row_5)
            with self.assertRaises(ProgrammingError):
                insert_row(db_name=MYSQL_DB, db_table='test_table', dict_values=rw.row_7)
            with self.assertRaises(ProgrammingError):
                insert_row(db_name=MYSQL_DB, db_table='test_table', dict_values=rw.row_8)
            with self.assertRaises(ProgrammingError):
                insert_row(db_name=MYSQL_DB, db_table='test_table', dict_values=rw.row_10)


    def test_3_delete_from_db_successful(self):
        """Checks if data will get deleted from db table by passing the specified id"""
        with self.mock_db_config:
            self.assertEqual(delete_row(db_name=MYSQL_DB, db_table='test_table', p_id=14),
                             "Deleted Successfully")
            self.assertEqual(delete_row(db_name=MYSQL_DB, db_table='test_table', p_id=34),
                             "Deleted Successfully")
            self.assertEqual(delete_row(db_name=MYSQL_DB, db_table='test_table', p_id=74),
                             "Deleted Successfully")

    def test_4_delete_from_db_unsuccessful(self):
        """Checks if specified id provided for delete operation is correct or not"""
        with self.mock_db_config:
            with self.assertRaises(ProgrammingError):
                delete_row(db_name=MYSQL_DB, db_table='test_table', p_id='')
            with self.assertRaises(ProgrammingError):
                delete_row(db_name=MYSQL_DB, db_table='test_table', p_id=[56])
            with self.assertRaises(ProgrammingError):
                delete_row(db_name=MYSQL_DB, db_table='test_table', p_id={'key': 'value'})

    def test_5_update_row_of_database_successful(self):
        """Checks if updating the row went successful"""
        with self.mock_db_config:
            self.assertEqual(update_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_3, p_id=67), "data updated successfully")
            self.assertEqual(update_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_5, p_id=15), "data updated successfully")
            self.assertEqual(update_row(db_name=MYSQL_DB, db_table='test_table',
                                        dict_values=rw.row_9, p_id=5), "data updated successfully")

    def test_6_update_row_of_db_unsuccessful(self):
        """Checks if updating the data throws exception while providing wrong inputs"""
        with self.mock_db_config:
            with self.assertRaises(ProgrammingError):
                update_row(db_name=MYSQL_DB, db_table='test_table', dict_values=rw.row_7, p_id=6)
            with self.assertRaises(DatabaseError):
                update_row(db_name=MYSQL_DB, db_table='test_table', dict_values=rw.row_8, p_id=90)
            with self.assertRaises(ProgrammingError):
                update_row(db_name=MYSQL_DB, db_table='test_table', dict_values=rw.row_10, p_id=90)

    def test_7_read_from_db_successful(self):
        """Checks if data read from table returns same number of rows as its actual in db"""
        with self.mock_db_config:
            self.assertEqual(view_data(db_name=MYSQL_DB, db_table='test_table')[1], 5)

    def test_8_read_from_db_unsuccessful(self):
        """Checks if db name or db table name is given correct or not"""
        with self.mock_db_config:
            with self.assertRaises(ProgrammingError):
                view_data(db_name=MYSQL_DB, db_table='data_table')
            with self.assertRaises(ProgrammingError):
                view_data(db_name=MYSQL_DB, db_table=768)
            with self.assertRaises(ProgrammingError):
                view_data(db_name='data_base', db_table=768)
