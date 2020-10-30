from celery import Celery
import celery_pubsub

worker = Celery('cpe', broker='redis://redis:6379/0')
# Now, let's publish something
res = celery_pubsub.publish('some.topic', data='something', value=42)

# We can get the results if we want to (and if the tasks returned something)
# But in pub/sub, usually, there's no result.
print(res.get())

# This will get nowhere, as no task subscribed to this topic
res = celery_pubsub.publish('nowhere', data='something else', value=23)
