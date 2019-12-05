"""Module docstring"""


class Worker:
    """
    Class to represent worker
    """
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Returns:
            Name of the worker
        """
        return self.name

    def take_task(self, task, log):
        """
        Take task and try to confirm it in log
        Args:
            task: task that worker try to confirm
            log: current log
        """
        log.confirm(self, task)


class Task:
    """class representing task with fixed payment"""
    def __init__(self, task_name, payment):
        self.task_name = task_name
        self.payment = payment
        self.completed = False

    def get_status(self):
        """
        Returns:
            Boolean. Status of task: completed or not completed
        """
        return self.completed

    def change_status(self):
        """
        Returns:
            Boolean. Changed status of task
        """
        self.completed = not self.completed

    def get_task_name(self):
        """
        Returns:
            Task name
        """
        return self.task_name

    def get_payment(self):
        """
        Returns:
            Payment for completing the task
        """
        return self.payment


class HourlyPaymentTask(Task):
    """Class to represent task with hourly payment"""
    def __init__(self, task_name, payment, time_to_complete):
        super().__init__(task_name, payment)
        self.time_to_complete = time_to_complete

    def get_payment(self):
        """
        Calculate payment for all time of work
        Returns:
            Payment for given time of work
        """
        return self.payment * self.time_to_complete


class Log:
    """Class to represent log"""
    def __init__(self):
        self.payments = {}

    def confirm(self, worker, task):
        """
        If task doesnt completed allow worker to complete it.
        Calculate total payment for worker and add it to log
        Args:
            worker:
            task:
        """
        if not task.get_status():
            task.change_status()
            if worker.get_name() not in self.payments:
                self.payments[worker.get_name()] = task.get_payment()
            else:
                self.payments[worker.get_name()] += task.get_payment()
            return "Confirmed"

        return "Rejected. Task already completed"

    def report(self):
        """
        Returns:
            Formed log report
        """
        return '\n'.join(f"{name}\t${payment}" for name, payment in self.payments.items())
