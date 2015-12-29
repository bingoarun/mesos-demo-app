from apscheduler.scheduler import Scheduler
from flask import Flask
import click

app = Flask(__name__)
count = 0
sched = Scheduler()
sched.start()
#Time out to reset count (in seconds)
time_limit=0
#Number of accepted connections in time_limit
max_connections=0

def clearCount():
    global count
    count=0
    print "Count set to 0"

sched.add_interval_job(clearCount, seconds = time_limit)

@click.command()
@click.option('--time', default=20, help='Time out to reset count (in seconds)')
@click.option('--max', default=5, help='Number of accepted connections in the specified time')
def initializeVar(time,max):
    global time_limit
    global max_connections
    time_limit,max_connections=time,max


@app.route('/')
def hello_world():
    global count
    count = count+1
    if count<=max_connections:
        return 'Hello World! %d' % count
    else:
        return 'Too much load :P '

if __name__ == '__main__':
    initializeVar()
    app.run(host='0.0.0.0',port='1234')