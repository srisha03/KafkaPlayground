# Kafka Playground

Kafka Playground is a beginner-friendly project aimed at understanding the fundamentals of Apache Kafka through a simple Flask application. This project allows you to send search queries from a Flask app to a Kafka topic, and a Kafka consumer reads and displays these messages.

## Architecture

[Insert diagram showing the flow from Flask App -> Kafka -> Consumer]

## Setup

### Environment Setup

1. **Java Installation**:
    - Kafka requires Java to run. Download and install the [Java JDK](https://www.oracle.com/java/technologies/javase-jdk15-downloads.html).

2. **Kafka Installation**:
    - Download the latest release of Apache Kafka from the [official website](https://kafka.apache.org/downloads).
    - Extract the Kafka binaries into a folder of your choice.

3. **Python Environment Setup**:
    - Ensure you have Python installed on your machine.
    - It's recommended to create a virtual environment for this project:
        ```bash
        python -m venv kafkaenv
        source kafkaenv/bin/activate  # On Windows use: kafkaenv\Scripts\activate
        ```

### Running Kafka

1. Open a command prompt and navigate to the Kafka directory.
2. Start Zookeeper:
    ```bash
    .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
    ```
3. In a new command prompt, start Kafka:
    ```bash
    .\bin\windows\kafka-server-start.bat .\config\server.properties
    ```

### Running the Flask App

1. Clone this repository to your local machine.
2. Navigate to the `flask-app` directory.
3. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask app:
    ```bash
    python app.py
    ```

### Running the Kafka Consumer

1. Navigate to the `kafka-setup` directory.
2. Run the Kafka consumer script:
    ```bash
    python consumer.py
    ```

## Learning Outcomes

Through this project, we will learn:

- How to setup and run Apache Kafka on your local machine.
- Basics of Kafka producers and consumers.
- How to integrate a simple Flask application with Kafka.
- How to observe the flow of messages through Kafka.

## Future State

- Explore Kafka monitoring tools for better visibility into your Kafka cluster.
- Setup a multi-broker Kafka cluster to understand Kafka’s distributed nature.
- Explore Kafka Streams for stateful stream processing.
- Learn about Kafka Connect for integrating with various data sources and sinks.
