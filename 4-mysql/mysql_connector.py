#!/usr/bin/python3
import random
from random import randint
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, db_port, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            port = db_port,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("127.0.0.1", "4406", "root", "master", "sm_app")

def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
     except Error as e:
         print(f"The error '{e}' occurred")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name VARCHAR(255) NOT NULL, 
  age INT, 
  gender VARCHAR(255),
  field1 VARCHAR(255),
  field2 VARCHAR(255),
  field3 VARCHAR(255),
  field4 VARCHAR(255),
  field5 VARCHAR(255),
  field6 VARCHAR(255),
  field7 VARCHAR(255),
  field8 VARCHAR(255),
  field9 VARCHAR(255),
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection, create_users_table)  

create_users = """
INSERT INTO
  users (name, age, gender, field1, field2, field3, field4, field5, field6, field7, field8, field9)
VALUES
  ('James', 25, 'male', 'USA', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'),
  ('Leila', 32, 'female', 'France', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'),
  ('Brigitte', 35, 'female', 'England', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'),
  ('Mike', 40, 'male', 'Denmark', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test'),
  ('Elizabeth', 21, 'female', 'Canada', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test');
"""

execute_query(connection, create_users) 