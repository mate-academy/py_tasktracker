import tasks


def test_report_one():
    log1 = tasks.Log()
    worker1 = tasks.Worker("Dima")
    worker2 = tasks.Worker("John")
    task1 = tasks.HourlyPaymentTask("Homework", 10, 3)
    task2 = tasks.Task("Take cup of tea", 5)
    worker1.take_task(task1, log1)
    worker2.take_task(task2, log1)
    assert log1.report() == 'Dima\t$30\nJohn\t$5'

def test_report_two():
    log1 = tasks.Log()
    worker1 = tasks.Worker("Dima")
    worker2 = tasks.Worker("John")
    task1 = tasks.HourlyPaymentTask("Homework", 10, 3)
    task2 = tasks.Task("Take cup of tea", 5)
    worker1.take_task(task1, log1)
    worker2.take_task(task2, log1)
    worker1.take_task(task1, log1)
    assert log1.report() == 'Dima\t$30\nJohn\t$5'

def test_report_three():
    log1 = tasks.Log()
    worker1 = tasks.Worker("Dima")
    worker2 = tasks.Worker("John")
    task1 = tasks.HourlyPaymentTask("Homework", 10, 3)
    task2 = tasks.Task("Take cup of tea", 5)
    task3 = tasks.Task("Web serfing", 25)
    worker1.take_task(task1, log1)
    worker2.take_task(task2, log1)
    worker1.take_task(task3, log1)
    assert log1.report() == 'Dima\t$55\nJohn\t$5'

def test_report_four():
    log1 = tasks.Log()
    worker1 = tasks.Worker("Dima")
    worker2 = tasks.Worker("John")
    worker3 = tasks.Worker("Bill")
    task1 = tasks.HourlyPaymentTask("Homework", 10, 3)
    task2 = tasks.Task("Take cup of tea", 5)
    task3 = tasks.Task("Web serfing", 25)
    worker1.take_task(task1, log1)
    worker2.take_task(task2, log1)
    worker3.take_task(task3, log1)
    assert log1.report() == 'Dima\t$30\nJohn\t$5\nBill\t$25'