from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    con.delete("country", "city")

    con.mset({"country": "德国", "city": "伦敦"})

    result = con.mget("country", "city")
    for i in result:
        print(i.decode("utf-8"))

except Exception as e:
    print(e)
finally:
    del con


