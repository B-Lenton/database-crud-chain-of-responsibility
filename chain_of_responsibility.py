"""
Chain of Responsibility: behaviour design pattern allowing requests to be passed along a chain of handlers; upon receiving the request, each handler decides to either (1) process it or (2) pass it on to the next handler.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import sqlite3
import sys

from readSongs import *
from searchSongs import *
from deleteSongs import *
from addSongs import *
from updateSongs import *

# TODO: Recreate database with new syntax to enable partial text matches https://www.sqlitetutorial.net/sqlite-full-text-search/
conn = sqlite3.connect(
    "/home/ben/Desktop/Just-IT/python/week11/project/c5Music.db"
    )
cursor = conn.cursor()


class Handler(ABC):
    """
    The Handler interface: Declares a method for building the chain of handlers.
    Also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior implemented inside base handler class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # handler1.set_next(handler2).set_next(handler3)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

# TODO: Add "help" and "request not recognised" handlers & create a domain-specific language for interacting with the program
class ReadSongsHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "1":
            return read_songs()
        else:
            return super().handle(request)


class AddSongsHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "2":
            return add_songs()
        else:
            return super().handle(request)


class UpdateSongsHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "3":
            return update_songs()
        else:
            return super().handle(request)


class SearchSongsHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "4":
            return search_songs()
        else:
            return super().handle(request)


class DeleteSongsHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "5":
            return delete_songs()
        else:
            return super().handle(request)


class ExitHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "6":
            print("Exiting")
            sys.exit(0)
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """
    choice = ""
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        print("\nMenu Options\n1. Print Songs\n2. Add Songs\n3. Update Songs\n4. Search Songs\n5. Delete Songs\n6. Exit")

        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Not in the list of options")

    print(f"You have chosen {choice}")
    handler.handle(choice)
    # if result:
    # print(f"{result}", end="")
    # else:
    #     print(f"Option {choice} failed.", end="")


if __name__ == "__main__":
    read_song = ReadSongsHandler()
    add_song = AddSongsHandler()
    update_song = UpdateSongsHandler()
    search_song = SearchSongsHandler()
    delete_song = DeleteSongsHandler()
    exit = ExitHandler()


    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Read > Add > Update...")
    
    program = True
    while program is True:
        read_song.set_next(add_song).set_next(update_song).set_next(search_song).set_next(delete_song).set_next(exit)
        client_code(read_song)
        print("\n")
        # if exit.handle("6"):
        #     print("Goodbye")
        #     program = False

    # print("Subchain: Add > Update...")
    # client_code(add_song)
