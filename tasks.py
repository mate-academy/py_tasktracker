"""implement a simple task tracker"""


class Worker:
    """Class worker, need worker name"""
    def __init__(self, name: str):
        self._name = name

    def __repr__(self):
        return self._name

    def confirm(self, task, log):
        """make record in log"""
        log.confirm(self, task)


class Task:
    """fixed payment task"""
    def __init__(self, task_name: str, payment: int, worker: Worker):
        self._worker = worker
        self._task_name = task_name
        self._payment = payment

    def __repr__(self):
        return self._task_name

    def __str__(self):
        return self._task_name

    def get_payment(self):
        """
        return payment for task
        """
        return self._payment

    def get_worker(self):
        """
        return worker who doing this task
        """
        return self._worker


class HourlyTask(Task):
    """hourly payment task"""
    def __init__(self, task_name: str, payment_per_hour: int, hours_worked: int, worker: Worker):
        super().__init__(task_name, payment_per_hour, worker)
        self._payment_per_hour = payment_per_hour
        self._hours_worked = hours_worked

    def get_payment(self):
        """
        return payment for task
        """
        return self._payment_per_hour * self._hours_worked


class Log:
    """
    Class for working with logs
    """
    def __init__(self):
        self._log = []

    def confirm(self, worker: Worker, task: Task):
        """
        Confirms the job and logs it.  If the work is done by another employee, return warning.
        """
        if worker is not task.get_worker():
            return f"task: {task} is not {worker} work"
        self._log.append({"worker": worker,
                          "task": task,
                          "payment": task.get_payment()})
        return True

    def report(self):
        """
        return all log list
        """
        result = ""
        for i in self._log:
            result += "{0}\t${1}\n".format(i["worker"], i["payment"])
        return result[:-1]
