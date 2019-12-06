"""
Module for keeping track of how much money earn workers,
solving tasks.
Classes
-------
Task
Log
Worker
"""


class Task:
    """
    A class that define type of the task and payment for this task
    Attributes
    ----------
    task_type : str  --  type of the task
    hours : float -- number of hours for hourly task

    Methods
    -------
    payment()
    """

    def __init__(self, task_type='fixed', hours=None):
        self.task_type = task_type.lower()
        self.hours = hours

    def payment(self):
        """Return payment that worker get for the task"""
        fixed_pay = 100
        hourly_rate = 10
        total = 0
        if self.task_type == 'fixed':
            return fixed_pay

        if self.task_type == 'hourly':
            try:
                total = self.hours * hourly_rate
            except TypeError:
                raise Exception("TypeError! Parameter hours not specified")
        return total

    def get_task_type(self):
        """Return type of the task"""
        return self.task_type


class Log:
    """
    Create report about all workers and their earning
    Attributes
    ----------
    database : dict  --  data base for all workers and earnings

    Methods
    -------
    report()
    """
    def __init__(self):
        self.database = {}

    def report(self):
        """Return report that contains workers names and earnings"""
        rep = ''
        for name, money in self.database.items():
            rep += f'{name}\t${money}\n'
        return rep

    def get_database(self):
        """Return database"""
        return self.database


class Worker:
    """
    A class that represent a worker
    Attributes
    ----------
    name : str  --  name of a worker

    Methods
    -------
    confirm(task, log)
    get_name()
    """
    def __init__(self, name):
        self.name = name

    def confirm(self, task: Task, log: Log):
        """Add worker and his payment to the database"""
        if self.name not in log.database.keys():
            log.database[self.name] = task.payment()
        else:
            log.database[self.name] += task.payment()

    def get_name(self):
        """Return name of the worker"""
        return self.name
