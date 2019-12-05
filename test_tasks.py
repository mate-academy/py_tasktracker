import tasks


def test_report():
    # Data initialization
    w1 = tasks.Worker("Bill", 5, True)
    w2 = tasks.Worker("John", 3, True)
    t1 = tasks.HourlyTask(w1, 4, True, 4)
    t2 = tasks.FixedTask(w2, 30, True)
    p1 = tasks.HourlyPaymentPerTask(w1, t1)
    p2 = tasks.FixedPaymentPerTask(w2, t2)
    l = tasks.Log(p1, p2)
    assert l.report() == """Bill\t$20
John\t$30"""