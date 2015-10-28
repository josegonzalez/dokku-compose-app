import flask
import os
import redis
import urlparse

dsn = urlparse.urlparse(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))
debug = os.getenv('DEBUG', '0').lower()
debug = True if debug in ['1', 'true', 'on'] else False
app = flask.Flask(__name__)
redis_client = redis.Redis(host=dsn.hostname, port=dsn.port)


@app.route('/')
def hello():
    redis_client.incr('hits')
    return 'Hello World! I have been seen {0} times.'.format(
        redis_client.get('hits')
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
