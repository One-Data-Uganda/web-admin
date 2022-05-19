import json
from operator import itemgetter

from app import redisConn
from app.core.logger import log


def fetchFromRedis(table, id):
    if id is None:
        return None

    row = redisConn.hget(table, id)
    if not row:
        return None

    return json.loads(row)


def fetchListFromRedis(table, idx=None):
    rows = redisConn.hgetall(table)
    if not rows:
        return None

    result = [json.loads(y) for x, y in rows.items()]
    try:
        if idx:
            result = sorted(result, key=itemgetter(idx))
    except Exception as e:
        log.error(e)

    return result


def pushListToRedis(table, rows):
    with redisConn.pipeline() as pipe:
        for r in rows:
            pipe.hset(table, r["id"], json.dumps(r))
        pipe.execute()


def pushToRedis(table, row):
    redisConn.hset(table, row["id"], json.dumps(row))


def removeFromRedis(table, id):
    redisConn.hdel(table, id)
