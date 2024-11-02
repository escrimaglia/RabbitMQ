# Consumer
# By Ed Scrimaglia

import pika

used_queue = 'cola_test'

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

def consume_messages():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue=used_queue)

        channel.basic_consume(queue=used_queue, on_message_callback=callback, auto_ack=True)

        print(' [*] Leyendo cola en RabbitMQ. To exit press CTRL+C')
        
        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError as err:
        print ("RabbitMQ connection error")
    except pika.exceptions.AMQPChannelError as err:
        print (f"RabbitMQ queue {used_queue} can not be used")
    except (Exception, KeyboardInterrupt) as err:
        print (err)

if __name__ == "__main__":
    consume_messages()
   
