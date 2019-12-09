"""
In this exercise you should implement a simple task tracker.
There are two kinds of tasks: fixed payment task and hourly
payment task. Any task can be assigned to a worker.
The worker has a name and can confirm task completion to the
log. The log should be able to produce reports with worker's
names and payment for completed tasks. You should offer your
own design for class relationships in this exercise.
"""


class Worker:
    """Class Worker accepts one argument - name"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Get name"""
        return self.name

    def set_name(self, name):
        """Set name"""
        self.name = name


class Task:
    """Class Task accepts one argument - status.
    'default fixed'"""
    def __init__(self, status='fixed'):
        self.status = status

    def get_status_task(self):
        """Get status Task"""
        return self.status

    def set__status_task(self, status):
        """Set status task"""
        self.status = status

    def calc_payment(self, time=1):
        """Calculate payment"""
        if self.status == 'fixed':
            return '$30'
        return '${}'.format(20*time)


class Log:
    """Class Log where all the work is recorded"""
    def __init__(self):
        self.register = Register()

    def confirm(self, worker: Worker, task: Task):
        """Confirm task"""
        self.register.add_task(worker, task)

    def report(self):
        """Report about task"""
        return self.register.get_register()


class Register:
    """Class Register where all the tasks are recorded"""
    def __init__(self):
        self.register = []

    def add_task(self, worker, task):
        """Add new task"""
        self.register.append([worker.get_name(), task.calc_payment()])

    def get_register(self):
        """Get register"""
        return '\n'.join(['\t'.join(lst) for lst in self.register])
