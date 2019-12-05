import tasks


def test_report():
    worker1 = tasks.Worker("Bill")
    worker2 = tasks.Worker("John")
    ftask = tasks.Task("go away", 20, worker1)
    htask = tasks.HourlyTask("go here", 15, 2, worker2)
    log = tasks.Log()
    log.confirm(worker1, ftask)
    log.confirm(worker2, htask)
    assert log.report() == """Bill\t$20
John\t$30"""
