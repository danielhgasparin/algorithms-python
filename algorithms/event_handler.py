"""Event handler module."""

class EventHandler:
    """Manages events and callbacks."""
    def __init__(self):
        self.events = dict()


    def on(self, event_name, callback):
        """Register an event handler."""
        self.events.setdefault(event_name, []).append(callback)


    def trigger(self, event_name):
        """Trigger all callbacks associated with the specified event name."""
        for fn in self.events.get(event_name, []):
            fn()


    def off(self, event_name):
        """Remove all callbacks associated with the specified event name."""
        del self.events[event_name]