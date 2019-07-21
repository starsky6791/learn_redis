import redis
from redis_db import pool
from concurrent.futures import ThreadPoolExecutor

try:
    def say_hello():
        print("hello")
    executor = ThreadPoolExecutor(50)
    for i in range(10):
        executor.submit(say_hello())
except Exception as e:
    print(e)

