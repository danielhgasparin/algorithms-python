import unittest
from algorithms.event_handler import *

class TestEventHandler(unittest.TestCase):
    def test_event_handler(self):
        
        def make_counter():
            count = 0
            def counter():
                nonlocal count
                count += 1
                return count
            return counter

        counter = make_counter()

        handler = EventHandler()
        handler.on("click", counter)
        handler.on("doubleclick", counter)
        handler.on("doubleclick", counter)
        handler.trigger("click")
        self.assertEqual(counter(), 2)
        handler.trigger("doubleclick")
        self.assertEqual(counter(), 5)
        handler.off("doubleclick")
        handler.trigger("doubleclick")
        self.assertEqual(counter(), 6)