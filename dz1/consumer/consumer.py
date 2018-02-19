import datetime
import pika
import psycopg2


while True:
    try:
        queue_connection = pika.BlockingConnection(
            pika.URLParameters("amqp://guest:guest@queue:5672")
        )
        database_connection = psycopg2.connect(
            "dbname=my_database user=consumer host=database"
        )
        break
    except:
        pass

channel = queue_connection.channel()
channel.queue_declare(queue='my_queue')

def callback(ch, method, properties, body):
    cursor = database_connection.cursor()
    now_time = datetime.datetime.now()
    received = (body.decode())
    cursor.execute("INSERT INTO queue_data VALUES (DEFAULT, %s, %s)",
                   (received, now_time)
    )
    database_connection.commit()
    cursor.close()

channel.basic_consume(callback,
            queue='my_queue',
            no_ack=True)

channel.start_consuming()

