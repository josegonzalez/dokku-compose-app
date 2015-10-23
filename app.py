import os

from flask import Flask
from redis import Redis
from urlparse import urlparse

dsn = urlparse(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))

app = Flask(__name__)
redis = Redis(host=dsn.hostname, port=dsn.port)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
