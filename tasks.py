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


class HourlyTask(Task):
    """
    Child class that inherit from Task and represents hourly
    task parameters which connected with each worker.
    """

    def __init__(self, worker: Worker, estimated_time: int,
                 completed: bool, total_task_hours: int):
        super().__init__(worker, estimated_time, completed)
        self.total_task_hours = total_task_hours

    def __str__(self) -> str:
        return f"HourlyTask(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})" \
               f"total_task_hours:{self.total_task_hours}"

    def __repr__(self) -> str:
        return f"HT<(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})" \
               f"total_task_hours:{self.total_task_hours}>"


class FixedTask(Task):
    """
    Child class that inherit from Task and represents fixed
    task parameters which connected with each worker.
    """

    def __init__(self, worker: Worker, total_task_payment,
                 completed: bool, estimated_time: int = 0):
        super().__init__(worker, estimated_time, completed)
        self.total_task_payment = total_task_payment

    def __str__(self) -> str:
        return f"FixedTask(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})" \
               f"total_task_payment:{self.total_task_payment}"

    def __repr__(self) -> str:
        return f"FT<(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})" \
               f"total_task_payment:{self.total_task_payment}>"


class Payment:
    """
    Parent class payment which contain information about every worker.
    """

    def __init__(self, worker: Worker):
        self.worker = worker

    def __str__(self) -> str:
        return f"Payment(worker:{self.worker}"

    def payment_result(self):
        """
        Return daily worker salary.
        :return: int
        """
        return self.worker.hourly_rate * self.worker.working_hours_per_day


class HourlyPaymentPerTask(Payment):
    """
    Child class that inherit from Payment and represents hourly payment
    parameters per task which connected with each worker and each worker task.
    """

    def __init__(self, worker: Worker, task: HourlyTask):
        super().__init__(worker)
        self.task = task

    def __str__(self) -> str:
        return f"HourlyPayment(worker:{self.worker}, task:{self.task}"

    def payment_result(self):
        """
        Return total payment from each hourly payment task.
        :return: int
        """
        if self.worker.presence_at_work \
                and self.task.completed \
                and self.task.total_task_hours >= self.task.estimated_hours:
            return self.task.total_task_hours * self.worker.hourly_rate
        return 0


class FixedPaymentPerTask(Payment):
    """
    Child class that inherit from Payment and represents fixed payment
    parameters per task which connected with each worker and each worker task.
    """

    def __init__(self, worker: Worker, task: FixedTask):
        super().__init__(worker)
        self.task = task

    def __str__(self) -> str:
        return f"FixedPayment(worker:{self.worker}, task:{self.task}"

    def payment_result(self):
        """
        Return total payment from each fixed payment task.
        :return: int
        """
        if self.worker.presence_at_work and self.task.completed:
            return self.task.total_task_payment
        return 0


class Log:
    """
    Log class represents information about task and worker
    which connected with each payment.
    """

    def __init__(self, *payments: Payment):
        self.payments = payments

    def __repr__(self) -> str:
        return f"<Log(payments:{self.payments})>"

    def confirm(self) -> dict:
        """
        Generate dict of items "worker name: task payment".
        :return: dict
        """
        task_payments = {}
        for payment in self.payments:
            if isinstance(payment, HourlyPaymentPerTask) \
                    and payment.payment_result() > 0:
                task_payments[payment.worker.name] = payment.payment_result()
            elif isinstance(payment, FixedPaymentPerTask) \
                    and payment.payment_result() > 0:
                task_payments[payment.worker.name] = payment.payment_result()
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
