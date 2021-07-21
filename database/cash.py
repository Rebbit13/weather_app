import os

from redis import Redis

cash = Redis(host="cash", port=os.environ['REDIS_PORT'], password=os.environ['REDIS_PASSWORD'])