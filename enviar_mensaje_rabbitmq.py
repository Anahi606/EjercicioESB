import pika

def enviar_mensaje_a_rabbitmq(mensaje):
    conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexion.channel()

    canal.queue_declare(queue='cola_de_mensajes', durable=True)

    canal.basic_publish(exchange='', routing_key='cola_de_mensajes', body=mensaje)

    print('Mensaje enviado a la cola')
    conexion.close()

if __name__ == "__main__":
    mensaje = 'Holaaa xd'
    enviar_mensaje_a_rabbitmq(mensaje)

