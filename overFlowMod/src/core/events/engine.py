from .types import Event

class EventSystem:
    def __init__(self):
        self.handlers: dict[type[Event], list] = dict()

    def subscribe(self, event_type: type[Event]):
        def decorator(handler):
            self.handlers.setdefault(event_type, []).append(handler)
            return handler
        return decorator
    
    def emit(self, event: type[Event]) -> None:
        handlers = self.handlers.get(type(event), [])
        for handler in handlers:
            handler(event)