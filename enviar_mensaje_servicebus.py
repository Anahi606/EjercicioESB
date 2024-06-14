from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Cadena de conexión a Service Bus, no la pongo ya que github no me deja subirla
servicebus_connection_string = "AÑADIR"
queue_name = "colap"

def enviar_mensaje(mensaje):
    # Crear un cliente de Service Bus
    with ServiceBusClient.from_connection_string(conn_str=servicebus_connection_string, logging_enable=True) as servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=queue_name)
        with sender:
            servicebus_message = ServiceBusMessage(mensaje)
            sender.send_messages(servicebus_message)
            print(f"Mensaje enviado a la cola: {mensaje}")

# Ejemplo de uso
if __name__ == "__main__":
    enviar_mensaje("Holaa xd")
