from azure.servicebus import ServiceBusClient
import smtplib
from email.mime.text import MIMEText

# Cadena de conexión a Service Bus, no la pongo ya que github no me deja subirla
servicebus_connection_string = "AÑADIR"
queue_name = "colap"

def enviar_correo(mensaje):
    #AÑADIR EL CORREO Y CONTRASEÑA DE APP, NO PONGO LA MIA YA QUE EL REPOSITORIO ES PUBLICO
    sender_email = "CORREO"
    app_password = "CONTRA"
    receiver_email = "CORREO al que llega"

    message = MIMEText(mensaje)
    message['Subject'] = 'Mensaje cola'
    message['From'] = sender_email
    message['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def recibir_mensaje():
    with ServiceBusClient.from_connection_string(conn_str=servicebus_connection_string, logging_enable=True) as servicebus_client:
        receiver = servicebus_client.get_queue_receiver(queue_name=queue_name)
        with receiver:
            for msg in receiver:
                mensaje_recibido = str(msg)
                print(f"Mensaje recibido: {mensaje_recibido}")
                enviar_correo(mensaje_recibido)
                receiver.complete_message(msg)

if __name__ == "__main__":
    recibir_mensaje()
