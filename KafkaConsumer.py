
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('foobar', b'some_message_bytes')
producer.flush()


from kafka import KafkaConsumer
#consumer = KafkaConsumer('test')
consumer = KafkaConsumer('test', bootstrap_servers='localhost:9092')
for msg in consumer:
    print (msg)
