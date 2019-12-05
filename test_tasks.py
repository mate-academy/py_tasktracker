import tasks


def test_report():
    # Data initialization
    w1 = tasks.Worker("Bill", 5, True)
    w2 = tasks.Worker("John", 3, True)
    t1 = tasks.HourlyPaymentTask(w1, 4, True, 4)
    t2 = tasks.FixedPaymentTask(w2, 30, True)
    l = tasks.Log(t1, t2)
    assert l.report() == """Bill\t$20
John\t$30"""