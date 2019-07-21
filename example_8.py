import redis
import random
from redis_db import pool

try:
    con = redis.Redis(connection_pool=pool)
    candi = ("马云", "马化腾", "李彦宏", "张朝阳", "丁磊")
    con.delete("ballot")
    con.zadd("ballot", {"马云": 0, "马化腾": 0, "张朝阳": 0, "李彦宏": 0, "丁磊": 0})
    for i in range(300):
        rand_num = random.randint(0, 4)
        con.zincrby("ballot", 1, candi[rand_num])
    result = con.zrevrange("ballot", 0, -1, withscores=True)
    for i in result:
        print(i[0].decode("utf-8"), int(i[1]))
except Exception as e:
    print(e)
finally:
    if "con" in dir():
        del con
