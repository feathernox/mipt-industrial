import pika
import random
import string


connection = pika.BlockingConnection(
    pika.URLParameters("amqp://guest:guest@queue:5672")
)
channel = connection.channel()
channel.queue_declare(queue='my_queue')
data = ''.join(random.choices(string.ascii_uppercase +
                              string.digits, k=10))
print(data)
channel.basic_publish(exchange='',
    routing_key='my_queue',
    body=data.encode()
)

connection.close()
