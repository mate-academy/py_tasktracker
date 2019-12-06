
class Worker:
    def __init__(self, worker_id, name):
        self.worker_id = worker_id
        self.name = name
        self.tasks = Register()

    def get_name(self):
        return self.name

    def approve(self, log, task):
        self.tasks.add_task(self, task)
        log.confirm(self, task)

    def get_worker_tasks(self):
        return self.tasks

    def __hash__(self):
        return hash(self.name) ^ hash(self.worker_id)

    def __str__(self):
        return f"{self.name}, {self.worker_id}"


class Task:
    def __init__(self, id_task, name, worker, sum_pay):
        self.id_task = id_task
        self.name = name
        self.worker = worker
        self.sum_pay = sum_pay

    def __hash__(self):
        return hash(self.worker) ^ hash(self.sum_pay)

    def __str__(self):
        return f"{self.name}: {self.worker.get_name()}, {self.sum_pay} "

    def get_name(self):
        return self.name

    def get_worker(self):
        return self.worker


class FTask(Task):
    def __init__(self, id_task, name, worker, sum_pay):
        super().__init__(id_task, name, worker, sum_pay)

    def get_sum_pay(self):
        return self.sum_pay


class HTask(Task):
    def __init__(self, id_task, name, worker, sum_pay, hours):
        super().__init__(id_task, name, worker, sum_pay)
        self.hours = hours

    def get_sum_pay(self):
        return self.hours * self.sum_pay


class Log:
    def __init__(self):
        self.logs = Register()

    def confirm(self, worker: Worker, task: Task):
        self.logs.add_task(worker, task)

    def report(self):
        return "\n".join(f"{task.get_name()},{worker.get_name()}: {task.get_sum_pay()}" for task, worker in self.logs)


class Register:
    def __init__(self):
        self.register_task = {}

    def add_task(self, worker, task):
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
