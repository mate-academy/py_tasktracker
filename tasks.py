"""In this exercise you should implement a simple task tracker. """


class Worker:
    """Worker representation"""
    def __init__(self, name):
        self.name = name

    def get_worker_name(self):
        """Returns worker name"""
        return self.name

    def report_about_task(self, log, task):
        """Report about completed task"""
        log.comfirm(self, task)


class Task:
    """Task representation"""
    def __init__(self, task, payment, task_type, rate, hours):
        self.task = task
        self.payment = payment
        self.task_type = task_type
        self.rate = rate
        self.hours = hours

    def get_task(self):
        """Returns task"""
        return self.task

    def get_salary(self):
        """Returns salary depending on type of task"""
        if self.task_type == 'Hourly':
            return self.rate * self.hours
        return self.payment


class Log:
    """Log represention"""
    def __init__(self):
        self.report_about_task = {}

    def confirm(self, worker: Worker, task: Task):
        """Fill info about worker's salary"""
        self.report_about_task[worker.name] = task.get_salary()

    def report(self):
        """Returns salary of every worker"""
        return '\n'.join("{}\t{}".format(k, v) for k, v in self.report_about_task.items())
