from app.poll import poll
from flask import current_app

@poll.route('/ping')
def ping():
    with current_app.app_context() as ctx:
        count = int(ctx.app.redis.get('poll-app') or 0)
        count += 1
        ctx.app.redis.set('poll-app', "{visits}".format(visits=count))

    return "Poll Successful... Polled for {number} times".format(number=count)