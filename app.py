from apscheduler.scheduler import Scheduler
from flask import Flask

app = Flask(__name__)
count = 0
sched = Scheduler()
sched.start()
#Time out to reset count (in seconds)
time_limit=20
#Number of accepted connections in time_limit
max_connections=5

def clearCount():
    global count
    count=0
    print "Count set to 0"

sched.add_interval_job(clearCount, seconds = time_limit)


@app.route('/')
def hello_world():
    global count
    print "count", count
    count = count+1
    if count<=max_connections:
        return 'Hello World! %d' % count
    else:
        return 'Too much load :P '

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='1234')