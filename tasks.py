'''
A simple task tracker
'''


class Worker:
    '''
    Worker class
    '''
    def __init__(self, name):
        self.name = name

    def get_task(self, task, log):
        '''
        Worker confirm task in log
        '''
        log.confirm(self, task)

    def get_name(self):
        '''
        return name
        '''
        return self.name


class Task:
    '''
    Parent class for task
    '''
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment

    def get_payment(self):
        '''
        Retyrn salary for task
        '''
        return self.payment

    def get_name(self):
        '''
        :return name of task
        '''
        return self.name


class HourlyTask(Task):
    '''
    Class for hoyrly class
    '''
    def __init__(self, task_name, payment, work_time):
        super().__init__(task_name, payment)
        self.work_time = work_time

    def get_payment(self):
        '''
        Reyrn salary for task
        '''
        return super().get_payment() * self.work_time


class Log:
    '''
    Log
    '''
    def __init__(self):
        self.info_log = {}

    def confirm(self, worker, task):
        '''
        Add worker and salary to log
        '''
        self.info_log[worker.name] = task.get_payment()

    def report(self):
        '''
        return all information about all warker and salary
        '''
        return '\n'.join(f"{name}\t${payment}" for name, payment in self.info_log.items())
