import psycopg2

#DB connection parameters
db_name="SMART_LIBRARY_DB"
db_user="admin"
db_password="admin"
db_host="postgres"

#connect to the database
conn=psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host
)

#create a cursor object
cursor = conn.cursor()

#example query
cursor.execute("SELECT version();")
record=cursor.fetchone()
print(f"you are connected to {record}")

cursor.close()
conn.close()