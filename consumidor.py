# Consumer
# By Ed Scrimaglia

import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

def consume_messages():
    # Establece onexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declara una cola (debe ser la misma que el publisher)
    channel.queue_declare(queue='cola_test')

    # Configura el consumidor para leer de la cola
    channel.basic_consume(queue='cola_test', on_message_callback=callback, auto_ack=True)

    print(' [*] Leyendo cola en RabbitMQ. To exit press CTRL+C')
    
    # Empieza a consumir mensajes
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()
