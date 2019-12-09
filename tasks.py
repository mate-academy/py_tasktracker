"""
In this program we can update
hourly/fixed tasks with a new ones
with a special price per each task
"""


class Task:
    """
    Parent object
    define Task object
    """
    def __init__(self, task_name):
        self._tasks = {**Hourly.tasks, **Fixed.tasks}
        self.task_name = task_name
        self._price = None

    def task_acceptable(self):
        """
        See we can accept this type of task
        :return:
        """
        return self._tasks

    def get_price(self):
        """
        Check what type of payment task has
        :return:
        """
        if self.task_name in Hourly.tasks:
            self._price = Hourly(self.task_name).price
        else:
            self._price = Fixed(self.task_name).price
        return self._price

    def get_rate(self):
        """
        Return total price
        :return:
        """
        self._price = self.get_price()
        return f"{self._price}$"


class Worker:
    """
    Worker objects
    We can update workers list
    """
    _workers = ['Bill', 'John', 'Ted']

    def worker_available(self):
        """
        Return workers list
        :return:
        """
        return self._workers

    def add_worker(self):
        """
        Add new worker
        :return:
        """
        new_worker = None
        self._workers += new_worker
        return self._workers


class Hourly(Task):
    """
    Task child object
    We can set random time
    for task completion
    """
    tasks = {'Task1': 10, 'Task2': 20}

    def __init__(self, task_name):
        super().__init__(task_name)
        self._time = 5  # random.randint(1, 11)
        self.price = self.tasks[self.task_name] * self._time


class Fixed(Task):
    """
    Task child object
    We can update tasks dict
    """
    tasks = {'Task3': 500}

    def __init__(self, task_name):
        super().__init__(task_name)
        # self.tasks = {'Task3': 500}
        self._time = 1
        self.price = self.tasks[self.task_name] * self._time


class Log:
    """
    Log object
    """
    def __init__(self, worker, task):
        self.worker = worker
        self.task = task
        self.worker_confirm = Worker()
        self.task_confirm = Task(self.task)
        self._confirm = False

    def confirm(self):
        """
        See if we can provide such worker and task
        :return:
        """
        if self.worker in self.worker_confirm.worker_available():
            if self.task in self.task_confirm.task_acceptable():
                self._confirm = True
        return self._confirm

    def report(self):
        """
        Ask user to pay
        :return:
        """
        if self.confirm():
            return f"Please pay {self.task_confirm.get_rate()} to {self.worker} for {self.task}!"
        return f"Worker or Task doesnt exists"
