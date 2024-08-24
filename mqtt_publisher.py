import asyncio
import aiomqtt

async def publish_message():
    async with aiomqtt.Client(
        hostname="localhost",  # Replace with your RabbitMQ server hostname if different
        port=1883,             # The MQTT port
        username="guest",      # Your RabbitMQ username
        password="guest"       # Your RabbitMQ password
    ) as client:
        
        # The message you want to send
        message1 = "message to topic1"
        message2 = "message to topic2"

        # Publish the message to topic1
        await client.publish("topic1", payload=message1)
        await client.publish("topic2", payload=message2)

        print(f"Message '{message1}' published to topic1")
        print(f"Message '{message2}' published to topic2")

if __name__ == "__main__":
    asyncio.run(publish_message())