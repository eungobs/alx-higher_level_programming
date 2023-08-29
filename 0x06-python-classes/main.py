#!/usr/bin/bash/python3
from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node

# Create a new linked list and insert some nodes
my_list = SinglyLinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)

# Print the linked list
my_list.print_list()
