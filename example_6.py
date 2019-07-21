import redis
from redis_db import pool

try:
    con = redis.Redis(connection_pool=pool)
    pipeline = con.pipeline()
    pipeline.watch("9527")
    pipeline.multi()
    con.hset("9527", "身高", 185)
    con.hset("9527", "体重", 90)
    pipeline.execute()
except Exception as e:
    print(e)
finally:
    if "pipeline" in dir():
        pipeline.reset()
    if "con" in dir():
        del con
