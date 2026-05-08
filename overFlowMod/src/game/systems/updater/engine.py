from typing import Callable
import time

class Task:
    def __init__(
        self,
        delta: float,
        callback: Callable
    ):
        self.delta = delta
        self.callback = callback
        self.last_update_time = time.monotonic()
    
    def update(self) -> None:
        now = time.monotonic()
        if now - self.last_update_time >= self.delta:
            self.callback()
            self.last_update_time = now

class Updater:
    def __init__(self):
        self.tasks: list[Task] = list()
    
    def every(self, delta: float):
        def decorator(func):
            task = Task(delta=delta, callback=func)
            self.tasks.append(task)
            return func
        return decorator

    def update(self) -> None:
        for task in self.tasks:
            task.update()