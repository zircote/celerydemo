from celerydemo.tasks import group_task, chord_task, chord_b
from celery import chord, group

def example_1():
    """
    Creates a chord/group combo that is executes(sent) with the delay call
    """
    tasks = (group_task.s(i, i) for i in xrange(10))
    chd = chord(group(tasks), chord_task.s())
    result = chd.delay()
    result.get()
    list(result.collect())


def example_2():
    """
    Creates a group that is finalized by a chord with the collective result of the group as the args
    This chord is executes upon creation
    """
    tasks = (group_task.s(i, i) for i in xrange(10))
    result = chord(tasks)(chord_task.s())
    result.get()
    list(result.collect())


def example_3():
    """
    Creates a group that is finalized as an immutable chord
    """
    tasks = (group_task.s(i, i) for i in xrange(10))
    result = chord(tasks)(chord_b.si())
    result.get()
    list(result.collect())


def get_it(start_id, max_id, record_count=200000):
    """
    :param start_id: interation start
    :param max_id: end of iteration
    :param record_count: the total records per iteration
    """
    iteration = start_id
    while iteration < max_id:
        start_id = iteration
        iteration = start_id + (100 * record_count)
        yield start_id, iteration - 1

