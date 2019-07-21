from redis_db import pool
import redis
from concurrent.futures import ThreadPoolExecutor
import random

consumer = set()
while True:
    if len(consumer) == 1000:
        break
    rand_num = random.randint(10000, 100000)
    set.add(rand_num)

try:
    con = redis.Redis(connection_pool=pool)
    con.delete("kill_num", "kill_total", "kill_users", "kill_flag")
    con.sadd("kill_users")
    con.mset({"kill_num": 0, "kill_total": 0})
    con.setex("kill_flag", 600, 1)
except Exception as e:
    print(e)
finally:
    if "con" in dir():
        del con

executor = ThreadPoolExecutor(200)
try:
    def buy():
        connection = redis.Redis(connection_pool=pool)
        pipeline = connection.pipeline()
        try:
            if pipeline.exists("kill_flag"):
                kill_num = int(connection.get("kill_num").decode("utf-8"))
                kill_total = int(connection.get("kill_total").decode("utf-8"))
                if kill_num < kill_total:
                    pipeline.multi()
                    pipeline.
                    pipeline.execute()



        except Exception as e:
            print(e)


            pipeline.watch("kill_num", "kill_users")
            pipeline.multi()
            connection.incr("kill_num")
            connection.


            pipeline.execute()
except Exception as e:
    print(e)

finally:
    if "pipeline" in dir():
       pip
