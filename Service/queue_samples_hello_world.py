# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: queue_samples_hello_world.py

DESCRIPTION:
    These samples demonstrate common scenarios like instantiating a client,
    creating a queue, and sending and receiving messages.

USAGE:
    python queue_samples_hello_world.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_STORAGE_CONNECTION_STRING - the connection string to your storage account
"""


import os
import sys
from azure.storage.queue import QueueClient

class QueueHelloWorldSamples:
    def __init__(self):
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    def create_client_with_connection_string(self):
        if self.connection_string is None:
            print("Missing required environment variable(s). Please set AZURE_STORAGE_CONNECTION_STRING.")
            sys.exit(1)

    def queue_and_messages_example(self, queue_name):
        if self.connection_string is None:
            print("Missing required environment variable(s). Please set AZURE_STORAGE_CONNECTION_STRING.")
            sys.exit(1)

        # Instantiate the QueueClient from a connection string
        queue = QueueClient.from_connection_string(conn_str=self.connection_string, queue_name=queue_name)

        # Create the queue
        queue.create_queue()

        try:
            # Send messages
            queue.send_message("I'm using queues!")
            queue.send_message("This is my second message")

            # Receive the messages
            response = queue.receive_messages(messages_per_page=2)

            # Print the content of the messages
            for message in response:
                print(message.content)

        finally:
            print("Queue process completed.")

    def delete_queue_do(self, queue_name):
        if self.connection_string is None:
            print("Missing required environment variable(s). Please set AZURE_STORAGE_CONNECTION_STRING.")
            sys.exit(1)

        # Instantiate the QueueClient from a connection string
        queue = QueueClient.from_connection_string(conn_str=self.connection_string, queue_name=queue_name)

        try:
            # Receive the messages (if any)
            response = queue.receive_messages(messages_per_page=2)

            # Print the content of the messages
            for message in response:
                print(message.content)

            # Delete the queue
            queue.delete_queue()

        finally:
            print(f"Queue '{queue_name}' deleted.")

            
if __name__ == '__main__':
    sample = QueueHelloWorldSamples()
    sample.create_client_with_connection_string()
    sample.queue_and_messages_example()
