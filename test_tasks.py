import tasks


def test_report():
    w1 = tasks.Worker(1, "bill")
    w2 = tasks.Worker(2, "tom")
    w3 = tasks.Worker(3, "arnold")

    t1 = tasks.FTask(1, "taskkk1", w1, 34)
    t2 = tasks.FTask(2, "taskkk2", w1, 10)
    t3 = tasks.HTask(3, "taskkk3", w3, 5, 10)

    l = tasks.Log()

    w1.approve(l, t2)
    w2.approve(l, t1)
    w2.approve(l, t3)
