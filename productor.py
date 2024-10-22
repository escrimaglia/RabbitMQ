# Consumer
# By Ed Scrimaglia

import pika
import os
import subprocess

def publish_message(message, queue_name='cola_test', host='localhost'):
    
    # Establecer conexión con RabbitMQ
    connection_parameters = pika.ConnectionParameters(host)
    with pika.BlockingConnection(connection_parameters) as connection:
        channel = connection.channel()

        # create cola en RabbitMQ
        channel.queue_declare(queue=queue_name)

        # Publica el mensaje
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f" [x] Sent '{message}'")


if __name__ == "__main__":
    # Opcion 1: Enviando a la cosa, la salida de consola
    cmd = 'ls -l'
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
    output, err = proc.communicate()
    publish_message(output)

    # Opcion 2: Mas simple, enviando a la cola un texto
    for _ in range(10):
        publish_message(f"Hello, Soy Ed y estoy publicando el mensaje {_}")