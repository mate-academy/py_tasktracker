import tasks


def test_report():
    return """Bill\t$20
John]t$30"""


def test():
    worker = tasks.Worker("John")
    worker2 = tasks.Worker("Uasya")
    ftask = tasks.Task("go_away", 500, worker2)
    assert ftask.get_payment() == 500
    htask = tasks.HourlyTask("go_here", 25, 5, worker)
    assert htask.get_payment() == 125
    log = tasks.Log()
    log.confirm(worker, htask)
    assert str(log.report()) == "[{'worker': John, 'task': go_here, 'payment': 125}]"
    assert log.confirm(worker, ftask) == "task: go_away is not John work"
