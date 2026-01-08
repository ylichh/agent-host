#!/usr/bin/env python
import pika
import uuid
import json
from src.adapters.langchain.i_tool import ILangTool

EXCHANGE_NAME = "climate_exchange"
QUEUE_NAME = "rpc_queue"


class RabbitMQClient(object):

    def __init__(
        self,
        rabbitmq_server: str,
        rabbitmq_port: int,
        rabbitmq_username: str,
        rabbitmq_password: str,
    ):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=rabbitmq_server,
                port=rabbitmq_port,
                credentials=pika.PlainCredentials(
                    username=rabbitmq_username, password=rabbitmq_password
                ),
            )
        )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call_available_cities(self):
        print("executing call available cities")
        return self.call_method("get_cities", {})

    def call_climate(self, ciudad):
        print("Executing climate call")
        body = {"ciudad": ciudad}
        return self.call_method("get_climate_info", body)

    def execute(self, ciudad):
        return self.call_climate(ciudad)

    def call_method(self, routing_key, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=routing_key,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body).encode("utf-8"),
        )
        while self.response is None:
            self.connection.process_data_events(time_limit=None)
        return json.loads(self.response)


if __name__ == "__main__":
    cliente = RabbitMQClient()
    print(cliente.call_climate("parís"))
