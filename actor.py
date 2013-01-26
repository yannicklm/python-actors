import threading
import queue

def actor(f):
    res = Actor(f.__name__)
    res.fun = f
    return res


def run(*actors):
    [actor.start() for actor in actors]
    [actor.join() for actor in actors]

class Actor(threading.Thread):
    work_queue = queue.Queue()
    def __init__(self, name):
        super().__init__(name=name)

    def push(self, value):
        self.work_queue.put(value)

    def pop(self):
        return self.work_queue.get()

    def run(self):
        try:
            while True:
                self.fun()
        except Exception as e:
            print(e)

