"""Task tracker"""


class Task:
    """Class of task
    By default all tasks are fixed payment,
    unless explicitly indicated hourly payment task
    """
    def __init__(self, payment, estimate, is_hourly_pay=False):
        self.payment = payment
        self.estimate = estimate
        self.is_hourly_pay = is_hourly_pay

    def get_payment_type(self):
        """Get type of payment"""
        if self.is_hourly_pay:
            return 'It is hourly payment task'
        return 'It is fixed payment task'

    def get_estimate(self):
        """Get estimate"""
        return self.estimate


class Worker:
    """Class of worker"""
    def __init__(self, name):
        self.name = name

    def complete_task(self, task, log):
        """Only worker can confirm task completion"""
        log.confirm(self, task)

    def get_name(self):
        """Get name of worker"""
        return self.name


class Log:
    """Class of the log"""
    def __init__(self):
        self.complete_tasks = {}

    def confirm(self, worker: Worker, task: Task):
        """Confirm task completion """
        payment = task.payment
        if task.is_hourly_pay:
            payment *= task.estimate
        self.complete_tasks[worker.name] = payment

    def report(self):
        """Get report of completed tasks"""
        report = ''
        for key, val in self.complete_tasks.items():
            report += '{0}\t{1}\n'.format(key, val)
        return report
