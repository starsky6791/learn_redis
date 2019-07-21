from redis_db import pool
import redis

try:
    con = redis.Redis(connection_pool=pool)
    con.hmset("9527", {"name": "王刚", "age": 27, "gender": "male"})
    con.hset("9527", "job", "销售")
    result = con.hgetall("9527")
    print(result.values())
    for i in result:
        print(i.decode("utf-8"), result[i].decode("utf-8"))
except Exception as e:
    print(e)

finally:
    del con
