from celeryconfig import app

from celery import chord, group

@app.task
def group_task(a, b):
    import time
    time.sleep(20)
    print '%s::%s' % (a, b)


@app.task
def chord_task(numbers):
    return sum(numbers)


@app.task
def chord_b():
    print 'Chord done'


@app.task
def gthis(start, end):
    print start, end


def get_it(start_id, max_id, record_count=200000):
    iteration = start_id
    while iteration < max_id:
        start_id = iteration
        iteration = start_id + (100 * record_count)
        yield start_id, iteration - 1


@app.task(bind=True)
def startup(self):
    # We can put the chord into a sbtask to automatically manage the chord
    #  By doing this we don't manually need to check that the chord is finished
    tasks = (group_task.s(a, b) for a, b in get_it(0, 100000, 100))

    # We need to pass the chord to ourselves as an iterable item 
    #  a list in this case
    result = self.subtask(
            [chord(tasks)(chord_b.si())]
    )
    return result
