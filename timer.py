import time 
from contextlib import contextmanager

@contextmanager
def cm_timer1():
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f'"Время работы блока: "{end - start:.6f} секунд')

class cm_timer2:
    def __init__(self):
        self.start = 0
        self.end = 0


    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            print(exc_type, exc_value, tb)
        self.end = time.perf_counter()
        print(f"Время работы блока {self.end-self.start:.6f} секунд")
