"""This is a program that defines interrelation between
tasks, their executors and respective report produced"""


class Log:
    """This class represents object that obtains inputs
    from class Worker objects and generates report
    based on those inputs and values from class Task"""

    def __init__(self):
        self.log_file = []

    def write_to_log(self, log_message):
        """Write the data reported by worker to the log"""
        self.log_file.append(log_message)

    def get_report(self):
        """Take all the tuples with workers' logs from the log file,
         calculate and report amount to be paid to worker. The same
         formulae used both for fixed payment tasks and for per hour tasks
         as by-default time input for fixed payment tasks is equal to 1"""
        report = ""
        for item in self.log_file:
            report += f"{item[0]} earned ${item[1][1] * item[2]}\n"
            # I know SoC principle is broken here (the same function
            # calculates and reports) but this approach seems to be logical
            # from OOP point of view as neither worker him/herself nor task
            # should be responsible for the payment
        return report


class Worker:
    """This class represents an object that has its own identity,
    obtains tasks (with automatic task plan update) and adds log
    for the tasks executed"""
    def __init__(self, name):
        """Initiate the worker"""
        self.name = name
        self.current_task = None

    def get_name(self):
        """Provide worker's name"""
        return self.name

    def get_task_from_dp(self, daily_plan):
        """Obtain the task from the task list (DailyPlan) on LIFO basis
        and update the list by removing the task obtained"""
        self.current_task = daily_plan.provide_task_to_worker()

    def get_current_task(self):
        """Provide the task taken from daily plan"""
        return self.current_task

    def log_task(self, log, dp_task, time_spent=1):
        """Generate the log for the task executed. Assume workers are responsible
        and provide fair and correct info on task execution:
        2 arguments for fixed payment tasks or 3 arguments
        for per-hour-payment tasks"""
        log_message = (self.name, dp_task, time_spent)
        log.write_to_log(log_message)

        # if dp_task == self.current_task:
        #     log.check_log += log_message
        # else:
        #     print("""That's not your task.
        #           Get the new task from the Daily Plan or
        #           input the name of task executed correctly""")


class Task:
    """This class objects maintain and provide the requisites of the task"""
    def __init__(self, name: str, rate: int):
        """Initiate the task with name and rate"""
        self.name = name
        self.rate = rate

    def get_name(self):
        """Provide the name of the task"""
        return self.name

    def get_rate(self):
        """Provide the rate of the task"""
        return self.rate


class DailyPlan:
    """This class objects collect
    and maintain the list of tasks to be executed"""
    def __init__(self):
        """Initiate the empty list"""
        self.tasks = []

    def create_plan(self, *to_be_created: Task):
        """Fill the list of tasks to be executed"""
        return self.tasks.extend((task.name, task.rate)
                                 for task in to_be_created)

    def provide_task_to_worker(self):
        """Eliminate last task input from the daily plan
        as it has already been assigned to worker"""
        return self.tasks.pop()

    def get_plan(self):
        """Provide daily plan being recent list of tasks"""
        return self.tasks
