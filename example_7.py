from redis_db import pool
import redis

try:
    con = redis.Redis(connection_pool=pool)
    file = open("student_info.txt", mode="r", encoding="utf-8", newline="")
    data = file.readlines()
    for one in data:
        print(one.split(","))
        result = one.split(",")
        sid = result[0]
        name = result[1]
        class_no = result[2]
        chinese = result[3]
        math = result[4]
        english = result[5]
        if int(math) > 85 and int(chinese) > 85 and int(english):
            con.hmset(sid, {"name": name, "class_no": class_no, "chinese": chinese, "math": math, "english": english})
except Exception as e:
    print(e)

finally:
    del con
    if "data" in dir():
        file.close()
