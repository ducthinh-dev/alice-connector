import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import MySQLConnection


class Connector:
    def __init__(self) -> None:
        load_dotenv()
        self.__DATABASE_HOST = os.environ.get("DATABASE_HOST")
        self.__DATABASE_SCHEMA = os.environ.get("DATABASE_SCHEMA")
        self.__DATABASE_USER = os.environ.get("DATABASE_USER")
        self.__DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
        self.__connection = self.__establish_connection()

    def __establish_connection(self):
        connection = MySQLConnection(user=self.__DATABASE_USER,
                                     password=self.__DATABASE_PASSWORD,
                                     host=self.__DATABASE_HOST,
                                     port=3306,
                                     database=self.__DATABASE_SCHEMA)
        return connection

    def refresh_connection(self):
        self.__connection = self.__establish_connection()

    def close_connection(self):
        self.__connection.close()

    def query_data(self, query: str):
        try:
            with self.__connection.cursor() as cursor:
                cursor.execute(query)
                raw_data = cursor.fetchall()
                raw_columns = cursor.column_names
            return (raw_columns, raw_data)
        except mysql.connector.Error as error:
            print(f"Oh no, {error}")

    def insert_data(self, table: str, data: list, column_names: list):
        try:
            columns = ", ".join(column_names)
            columns_len = len(column_names)
            values_marker = "%s"
            statement = (
                f"INSERT INTO {table} "
                f"({columns}) "
                f"VALUES ({', '.join([values_marker] * columns_len)})"
            )
            with self.__connection.cursor() as cursor:
                cursor.executemany(statement, data)
                self.__connection.commit()
        except mysql.connector.Error as error:
            print(error,
                  sep="\n")
