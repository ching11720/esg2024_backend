#!/usr/bin/env python
import pika, sys, os

def main():
    rabbitmq_user = "user"
    rabbitmq_password = "carbon2024"
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, 'my_vhost', pika.PlainCredentials(rabbitmq_user, rabbitmq_password)))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)