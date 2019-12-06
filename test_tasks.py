import tasks


def test_report():
    worker_1 = tasks.Worker('Bill')
    worker_2 = tasks.Worker('John')
    task_1 = tasks.Task('fixed')
    task_2 = tasks.Task('hourly', hours=3)
    task_3 = tasks.Task()
    log = tasks.Log()
    worker_1.confirm(task_1, log)
    worker_2.confirm(task_2, log)
    worker_2.confirm(task_3, log)
    log.report()
    return """Bill\t$100
John\t$130"""