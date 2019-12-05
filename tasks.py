"""
my own implementation of classes that represents tasks, workers and etc.
"""


class Worker:
    """
    Class represents worker.
    """

    def __init__(self, name: str, hourly_rate: int, presence_at_work: bool):
        self.name = name
        self.hourly_rate = hourly_rate
        self.working_hours_per_day = 8
        self.presence_at_work = presence_at_work

    def __str__(self) -> str:
        return f"Worker(name:{self.name}, hourly_rate:{self.hourly_rate}, " \
               f"working_hours_per_day:{self.working_hours_per_day}," \
               f"presence_at_work:{self.presence_at_work})"

    def __repr__(self) -> str:
        return f"<(name:{self.name}, hourly_rate:{self.hourly_rate}, " \
               f"working_hours_per_day:{self.working_hours_per_day}," \
               f"presence_at_work:{self.presence_at_work})>"


class Task:
    """
    Parent class that represents task parameters which connected
    with each worker.
    """

    def __init__(self, worker: Worker, estimated_time: int, completed: bool):
        self.worker = worker
        self.title = ""
        self.estimated_hours = estimated_time
        self.completed = completed

    def __str__(self) -> str:
        return f"Task(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})"

    def __repr__(self) -> str:
        return f"<T(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})>"


class HourlyPaymentTask(Task):
    """
    Child class that inherit from Task and represents hourly payment
    task parameters which connected with each worker.
    """

    def __init__(self, worker: Worker, estimated_time: int,
                 completed: bool, total_task_hours: int):
        super().__init__(worker, estimated_time, completed)
        self.total_task_hours = total_task_hours

    def __str__(self) -> str:
        return f"HourlyPaymentTask(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})"

    def get_payment_hourly_task(self):
        """
        Return total payment from each hourly payment task.
        :return: int
        """
        if self.worker.presence_at_work \
                and self.completed \
                and self.total_task_hours >= self.estimated_hours:
            return self.total_task_hours * self.worker.hourly_rate
        return 0


class FixedPaymentTask(Task):
    """
    Child class that inherit from Task and represents fixed payment
    task parameters which connected with each worker.
    """

    def __init__(self, worker: Worker, total_payment,
                 completed: bool, estimated_time: int = 0):
        super().__init__(worker, estimated_time, completed)
        self._total_payment = total_payment

    def __str__(self) -> str:
        return f"FixedPaymentTask(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})"

    def get_payment_fixed_task(self):
        """
        Return total payment from each fixed payment task.
        :return: int
        """
        if self.worker.presence_at_work and self.completed:
            return self._total_payment
        return 0


class Log:
    """
    Log class represents hourly payment task parameters
    which connected with each task.
    """

    def __init__(self, *tasks: Task):
        self.tasks = tasks

    def __repr__(self) -> str:
        return f"<Log(name:{self.tasks})>"

    def confirm(self) -> dict:
        """
        Generate dict of items "worker name: task payment".
        :return: dict
        """
        task_payments = {}
        for task in self.tasks:
            if isinstance(task, HourlyPaymentTask) \
                    and task.get_payment_hourly_task() > 0:
                task_payments[task.worker.name] = task.get_payment_hourly_task()
            elif isinstance(task, FixedPaymentTask) \
                    and task.get_payment_fixed_task() > 0:
                task_payments[task.worker.name] = task.get_payment_fixed_task()
            else:
                return {}
        return task_payments

    def report(self):
        """
        Generate string report from confirm() method result.
        :return: str
        """
        final_report = ""
        for worker_name, task_payment in self.confirm().items():
            final_report += f"{worker_name}\t${task_payment}\n"
        return final_report.rstrip("\n")
