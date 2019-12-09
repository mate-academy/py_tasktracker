import tasks


def test_report_one():
    log = tasks.Log()
    worker_artem = tasks.Worker("Artem")
    worker_alex = tasks.Worker("Alex")
    worker_masha = tasks.Worker("Masha")
    masha_fixet_task = tasks.Task("Task1", 300)
    fixet_task = tasks.Task("Task2", 100)
    hoyrly_task = tasks.HourlyTask("Task3", 200, 3)
    worker_masha.get_task(masha_fixet_task, log)
    worker_artem.get_task(fixet_task, log)
    worker_alex.get_task(hoyrly_task, log)
    assert log.report() == 'Masha\t$300\nArtem\t$100\nAlex\t$600'