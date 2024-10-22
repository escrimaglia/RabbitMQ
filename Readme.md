# RabbitMQ en Docker

## Implementación del patrón Productor/Consumidor en Python 3.12

RabbitMQ es uno de los Messsage Brokers mas conocidos para la implementación del patrón Productor/Consumidor.

Otros son Kafka, Reddis, ActiveMQ, Python Message Service, etc

### Ejecutar el siguiente comando para crear el contenedor (requiere docker y la libreria pika instalados)

docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

-d: Ejecuta el contenedor en segundo plano (detached).
--name rabbitmq: Nombra el contenedor como rabbitmq para que sea fácil identificarlo.
-p 5672:5672: Expone el puerto estándar de RabbitMQ para el protocolo AMQP (puerto de mensajería).
-p 15672:15672: Expone el puerto 15672 para la interfaz web de gestión de RabbitMQ.
rabbitmq:management: imagen oficial de rabbitq

### Acceder el portal de gestion RabbitMQ

http://localhost:15672

Credenciales por defecto para acceder al portal de gestión:

Usuario: guest  
Contraseña: guest

### Ejecutar el consumidor en una ventana

python3 consumidor.py

### Ejecutar el prductor en otra ventana

python3 productor.py
