# rabbitmq_mqtt
Sample project to show how rabbitmq works with mqtt


## Installation
1. Pull and run rabbit container
```bash
docker run -it --rm --name rabbitmq -p 1883:1883 -p 15672:15672 -p 15692:15692 -p 5672:5672 rabbitmq:3.13.0-management
```
2. Activate mqtt plugin
```bash
docker exec rabbitmq rabbitmq-plugins enable rabbitmq_mqtt
```
3. Enable all flags including feature flag mqtt_v5
```bash
docker exec rabbitmq rabbitmqctl enable_feature_flag all
```
4. Inside the container install mosquitto-clients
```bash
apt -y install mosquitto-clients
```
5. Run mosquitto
```bash
mosquitto_sub -h "localhost" -p 1883 -t "topic1" -u guest -P guest
```
### Configure bindings

1. Go to [http://localhost:15672/](http://localhost:15672/) in your web browser.
2. Log in with your RabbitMQ credentials. (guest, guest)
3. Navigate to the **"Queues"** tab.
4. Add a new queue named **"hello"** if it doesn’t exist.
5. Go to the **"Exchanges"** tab.
6. Find the **"amq.topic"** exchange.
7. In the **"Bindings"** section, bind **"topic1"** to the **"hello"** queue.
   - **Routing key**: `"topic1"`
   - **Queue**: `"hello"`

### Run python scripts

1. Install requirements.txt
2. Run rabbit_receiver.py, mqtt_subscriber.py and then mqtt_publisher.py