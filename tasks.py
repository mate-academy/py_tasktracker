
class Log:
    def __init__(self):
        self.payment = {}

    def confirm(self, worker, task):
        if not task.get_state():
            task.change_state()
            worker.change_payment(task.get_cost())
            self.payment[worker.get_name()] = worker.get_payment()
        else:
            print("Rejected. Task is already completed")

    def report(self):
        print(self.payment)


class Worker:
    def __init__(self, name: str):
        self.name = name
        self.payment = 0

    def get_name(self):
        return self.name

    def take_task(self, task, log):
        if isinstance(task, Task) or isinstance(task, HourlyPaymentTask):
            log.confirm(self, task)
        else:
            raise ValueError

    def change_payment(self, value):
        self.payment += value

    def get_payment(self):
        return self.payment


class Task:
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
        self.completed = False

    def get_cost(self):
        return self.cost

    def get_state(self):
        return self.completed

    def change_state(self):
        self.completed = not self.completed

    def get_name(self):
        return self.name


class HourlyPaymentTask(Task):
    def __init__(self, cost, hours, name):
        super().__init__(cost, name)
        self.cost = cost
        self.hours = hours
        self.name = name

    def get_cost(self):
        return self.cost * self.hours
l1 = log()
w1 = Worker("dima")
t1 = Task(1)