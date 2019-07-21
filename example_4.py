from redis_db import pool
import redis

try:
    con = redis.Redis(connection_pool=pool)
    con.zadd("keyword", {"马云": 10, "张朝阳": 20, "马化腾": "30"})
    con.zincrby("keyword",10, "马云")
    result = con.zrange("keyword", 0, -1)
    for i in result:
        print(i.decode("utf-8"))

    con.zscore("keyword", "马云")

except Exception as e:
    print(e)
finally:
    del con
