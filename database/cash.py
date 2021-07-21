import os

from redis import Redis

cash = Redis(host=os.environ['APP_CASH_HOST'], port=os.environ['REDIS_PORT'], password=os.environ['REDIS_PASSWORD'])