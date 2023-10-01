import json
from kafka import KafkaConsumer

def main():
    consumer = KafkaConsumer(
        'test-topic',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',  # Start reading the topic from the beginning if no offset is stored for a partition
        group_id='my-group'
    )

    for message in consumer:
        message_value = message.value.decode('utf-8')
        message_data = json.loads(message_value)
        print(f"Received message: {message_data['search_term']} at {message_data['timestamp']} with offset {message.offset}")

if __name__ == "__main__":
    main()