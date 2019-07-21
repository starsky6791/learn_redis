import redis
from redis_db import pool

con = redis.Redis(
    connection_pool=pool
)

con.set("city", "伦敦")
city = con.get("city").decode("UTF-8")
print(city)

del con
