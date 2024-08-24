import asyncio
import aiomqtt

async def main():
    async with aiomqtt.Client(
        hostname="localhost",
        port=1883, 
        username="guest",
        password="guest"
    ) as client:
        
            await client.subscribe("topic2")

            async for message in client.messages:
                print(f"Received message: {message.payload.decode()} on topic {message.topic}")

if __name__ == "__main__":
    asyncio.run(main())