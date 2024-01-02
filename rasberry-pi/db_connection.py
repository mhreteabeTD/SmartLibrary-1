import psycopg2

#DB connection parameters
db_name="SMART_LIBRARY_DB"
db_user="admin"
db_password="admin"
db_host="postgres"

#connect to the database
class DBConnection:
    def __init__(self):
        self.conn=psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host
        )

        #create a cursor object
        self.cursor = self.conn.cursor()

    def query(self,cmd):

        self.cursor.execute(cmd)
        return self.cursor.fetchall()
        