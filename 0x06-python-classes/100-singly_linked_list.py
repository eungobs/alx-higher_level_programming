#!/usr/bin/python3
"""Singly linked list module
"""


class Node:
    """Class defined for singly linked list node.

    Args:
        data (int): integer value to be stored in node
        next_node (Node): next node in linked list

    Attributes:
        __data (int): integer value stored in node
        __next_node (Node): next node in linked list

    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """__data getter, setter with same method name

        Returns:
            __data (int): integer value stored in node

        """
        return self.__data

    @data.setter
    def data(self, value):
        """Args:
            value (int): integer value to be stored in node

        Attributes:
            __data (int): integer value stored in node

        Raises:
            TypeError: if value is not an integer

        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """__next_node getter, setter with same method name

        Returns:
            __next_node (Node): next node in linked list

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Args:
            value (Node): next node in linked list

        Attributes:
            __next_node (Node): next node in linked list

        Raises:
            TypeError: if value is not a Node object or None

        """
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Class defined for singly linked list.

    Attributes:
        __head (Node): first node in linked list

    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): integer value to be stored in new Node

        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        curr_node = self.__head
        while curr_node.next_node is not None and curr_node.next_node.data < value:
            curr_node = curr_node.next_node
        new_node.next_node = curr_node.next_node
        curr_node.next_node = new_node

    def __str__(self):
        """Returns a string representation of the entire list.

        Returns:
            list_str (str): string representation of the entire list

        """
        curr_node = self.__head
        list_str = ''
        while curr_node is not None:
            list_str += str(curr_node.data) + '\n'
            curr_node = curr_node.next_node
        return list_str[:-1]
