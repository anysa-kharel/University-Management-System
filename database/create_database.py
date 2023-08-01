#You will need to install mysql-connector-python library to interact with MySql
#---->python pip install mysql-connector-python<------#

import mysql.connector

dataBase = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password =""
            )

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE uni_mngt_sys")
