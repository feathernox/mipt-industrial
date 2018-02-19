import datetime
import psycopg2


while True:
    try:
        database_connection = psycopg2.connect(
            "dbname=my_database user=reader host=database"
        )
        break
    except:
        pass

cursor = database_connection.cursor()
cursor.execute("SELECT * FROM queue_data")
for record in cursor:
    print(record)
cursor.close()

