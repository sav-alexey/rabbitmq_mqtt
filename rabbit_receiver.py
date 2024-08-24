import pika

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

def main():
    # Connection parameters for RabbitMQ
    connection_params = pika.ConnectionParameters(
        host='localhost',  # Replace with your RabbitMQ server hostname if different
        credentials=pika.PlainCredentials('guest', 'guest')
    )
    
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Ensure the queue exists
    channel.queue_declare(queue='hello')
    
    channel.queue_bind(exchange='amq.topic', queue='hello', routing_key='topic1')

    # Subscribe to the queue and define the callback
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print("Waiting for messages in 'hello' queue. To exit press CTRL+C")
    
    # Start consuming messages
    channel.start_consuming()

if __name__ == "__main__":
    main()