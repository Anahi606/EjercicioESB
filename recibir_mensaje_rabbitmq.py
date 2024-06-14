import pika
import os
import smtplib
from email.mime.text import MIMEText

# Cargar variables de entorno para el correo SMTP
#AÑADIR EL CORREO Y CONTRASEÑA DE APP, NO PONGO LA MIA YA QUE EL REPOSITORIO ES PUBLICO
usuario_smtp = os.getenv('CORREO')
clave_smtp = os.getenv('CLAVE')

def subscriptor(mensaje):
    servidor_smtp = 'smtp.office365.com'
    puerto_smtp = 587
    destinatario = 'CORREO al que llega'

    msg = MIMEText(mensaje)
    msg['Subject'] = 'Mensaje cola'
    msg['From'] = usuario_smtp
    msg['To'] = destinatario

    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(usuario_smtp, clave_smtp)
    servidor.sendmail(usuario_smtp, destinatario, msg.as_string())
    servidor.quit()

    print('Correo electronico enviado')

def callback(ch, method, properties, body):
    print('Mensaje recibido:', body.decode())
    subscriptor(body.decode())

def recibir_mensajes_de_rabbitmq():
    conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexion.channel()
    canal.queue_declare(queue='cola_de_mensajes', durable=True)

    print('Gestor de colas iniciado. Esperando mensajes...')
    
    canal.basic_consume(queue='cola_de_mensajes', on_message_callback=callback, auto_ack=True)
    canal.start_consuming()

if __name__ == "__main__":
    recibir_mensajes_de_rabbitmq()

