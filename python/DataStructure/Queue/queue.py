class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            value = self.queue[0]
            self.queue.remove(value)
            return value

    def peek(self) -> int:
        if self.queue:
            return self.queue[0]
        
    def empty(self) -> bool:
        return len(self.queue) == 0