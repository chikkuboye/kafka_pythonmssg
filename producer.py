from kafka import KafkaProducer

bootstrap_server = ["localhost:9092"]

topic = "nestData"

producer = KafkaProducer(bootstrap_servers = bootstrap_server)

producer = KafkaProducer()

data = "hello kafka from python"

message = producer.send(topic,bytes(data,"utf-8"))

metadata = message.get()

print(metadata.topic)
print(metadata.partition)