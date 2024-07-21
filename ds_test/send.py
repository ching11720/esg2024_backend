import pika
import os

rabbitmq_user = "user"
rabbitmq_password = "carbon2024"

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, 'my_vhost', pika.PlainCredentials(rabbitmq_user, rabbitmq_password)))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
