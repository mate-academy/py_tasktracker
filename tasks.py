"""There are two kinds of tasks: fixed payment task and hourly payment task.
 Any task can be assigned to a worker.
  The worker has a name and can confirm task completion to the log.
 The log should be able to produce reports with worker's names and payment for completed tasks."""


class Worker:
    """Worker has id, name and can approve task"""
    def __init__(self, worker_id, name):
        self.worker_id = worker_id
        self.name = name
        self.tasks = Register()

    def get_name(self):
        """get worker name"""
        return self.name

    def approve(self, log, task):
        """add task into register list"""
        self.tasks.add_task(self, task)
        log.confirm(self, task)

    def get_worker_tasks(self):
        """get all worker tasks"""
        return self.tasks

    def __hash__(self):
        return hash(self.name) ^ hash(self.worker_id)

    def __str__(self):
        return f"{self.name}, {self.worker_id}"


class Task:
    """task has id, name, sum pay and worker"""
    def __init__(self, id_task, name, sum_pay):
        self.id_task = id_task
        self.name = name
        self.worker = None
        self.sum_pay = sum_pay

    def __hash__(self):
        return hash(self.worker) ^ hash(self.sum_pay)

    def __str__(self):
        return f"{self.name}: {self.worker.get_name()}, {self.sum_pay} "

    def get_name(self):
        """return task name"""
        return self.name

    def get_worker(self):
        """return worker task"""
        return self.worker


class FTask(Task):
    """fix price task"""
    def __init__(self, id_task, name, sum_pay):
        super().__init__(id_task, name, sum_pay)

    def get_sum_pay(self):
        """return fix price sum"""
        return self.sum_pay


class HTask(Task):
    """hourly rate task"""
    def __init__(self, id_task, name, sum_pay, hours):
        super().__init__(id_task, name, sum_pay)
        self.hours = hours

    def get_sum_pay(self):
        """return sum pay: hours * sum pay"""
        return self.hours * self.sum_pay


class Log:
    """log all tasks with workers"""
    def __init__(self):
        self.logs = Register()

    def confirm(self, worker: Worker, task: Task):
        """confirm task"""
        task.worker = worker
        self.logs.add_task(worker, task)

    def report(self):
        """str representation"""
        return "\n".join(f"{task.get_name()},{worker.get_name()}: {task.get_sum_pay()}" for task, worker in self.logs)


class Register:
    """container for task and workers. Base on dictionary"""
    def __init__(self):
        self.register_task = {}

    def add_task(self, worker, task):
        """add new task on dictionary"""
        self.register_task[task] = worker

    def __repr__(self):
        return f"{self.register_task}"

    def __iter__(self):
        return self

    def __next__(self):
        if not self.register_task:
            raise StopIteration
        return self.register_task.popitem()

    def __str__(self):
        return f"{self.register_task}"
