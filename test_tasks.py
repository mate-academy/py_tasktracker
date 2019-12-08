import tasks


def test_report():
    w1 = tasks.Worker(1, "bill")
    w2 = tasks.Worker(2, "tom")

    t1 = tasks.FTask(1, "task1", 34)
    t2 = tasks.FTask(2, "task2", 10)
    t3 = tasks.HTask(3, "task3", 5, 10)

    l = tasks.Log()

    w1.approve(l, t2)
    w2.approve(l, t1)
    w2.approve(l, t3)
    assert l.report() == "task3,tom: 50\n" \
                         "task1,tom: 34\n" \
                         "task2,bill: 10"
