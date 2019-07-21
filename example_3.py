from redis_db import pool
import redis

try:
    con = redis.Redis(connection_pool=pool)
    con.delete("部门名称")
    con.rpush("部门名称", "董事会", "秘书处")
    con.lpop("部门名称")
    result = con.lrange("部门名称", 0, -1)
    for i in result:
        print(i.decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con
