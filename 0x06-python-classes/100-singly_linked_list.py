#!/usr/bin/python3
"""Singly-linked list generation
"""

from node import Node


class SinglyLinkedList:
    """Class defined for singly linked list.

    Attributes:
        __head (Node): head of linked list

    """

    def __init__(self):
        """Attributes:
            __head (Node): head of linked list

        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): value of new Node to be inserted into list

        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list.

        Returns:
            str: string representation of linked list with one node number by line

        """
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
