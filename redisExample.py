import redis

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

# r.set('foo', 'bar')
print(r.get('foo'))
