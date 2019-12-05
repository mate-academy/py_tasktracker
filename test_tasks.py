import tasks


def test_report():
    worker1 = tasks.Worker("Bill")
    worker2 = tasks.Worker("John")
    log = tasks.Log()
    task_fixed = tasks.FixedPayment("build home", 20)
    task_per_h = tasks.PaymentPerHour("do nothing", 15, 2)
    worker1.take_task(task_fixed)
    worker2.take_task(task_per_h)
    worker2.confirm(task_per_h, log)
    worker1.confirm(task_fixed, log)
    assert log.report() == """Bill\t$20
John\t$30"""