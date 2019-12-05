"""implement a simple task tracker"""

from typing import List
import linked_list


class Worker:
    """Class worker, need worker name"""
    def __init__(self, name: str):
        self._name = name
        self._tasks_in_process: List[Task] = []
    def __repr__(self):
        return f"Worker: {self._name}"

    def confirm(self, task, log):
        """make record in log"""
        self._tasks_in_process.remove(task)
        log.confirm(self._name, task.get_name(), task.get_payment())

    def take_task(self, task):
        """Add task in _tasks_in_process list"""
        self._tasks_in_process.append(task)


class Task:
    """parent class task"""
    def __init__(self, task_name):
        self._task_name = task_name

    def __repr__(self):
        return f"Task: {self._task_name}"

    def get_name(self):
        """return task name"""
        return self._task_name

class FixedPayment(Task):
    """Fixed payment task class"""
    def __init__(self, task_name, payment):
        super().__init__(task_name)
        self._payment = payment

    def get_payment(self):
        """return task payment"""
        return self._payment

class PaymentPerHour(Task):
    """Payment per hour task class"""
    def __init__(self, task_name, payment_per_hour, hours_worked):
        super().__init__(task_name)
        self._payment_per_hour = payment_per_hour
        self._hours_worked = hours_worked

    def get_payment(self):
        """return task payment per hour * hours worked"""
        return self._payment_per_hour * self._hours_worked


class Log:
    """
    Class for working with logs
    """
    def __init__(self):
        self._array = linked_list.List()

    def confirm(self, worker_name, task_name, task_payment):
        """insert record in linked list"""
        self._array.insert(worker_name, task_name, task_payment)

    def report(self):
        """return string with all records from linked list"""
        log = self._array.state()
        result = []
        for record in log:
            result.append(f"{record.worker_name()}\t${record.task_payment()}")
        return "\n".join(result)
