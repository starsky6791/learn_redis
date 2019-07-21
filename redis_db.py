from redis import ConnectionPool
import redis

pool = ConnectionPool(
    host="localhost",
    port=6379,
    password=123456,
    db=0,
    max_connections=10
)

con = redis.Redis(connection_pool=pool)

