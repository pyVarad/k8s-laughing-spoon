from app.config import Config
from flask import Flask
import redis



def create_app(appConfig=None):
    app = Flask(__name__)
    app.config.from_object(appConfig)

    with app.app_context() as ctx:
        ctx.app.redis = redis.Redis(
            host = 'redis',
            port = 6379,
            charset="utf-8", 
            decode_responses=True
        )

    from app.poll import poll
    app.register_blueprint(poll)

    return app

application = create_app(Config)
