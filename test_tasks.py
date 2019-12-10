import tasks


def test_tasks_creation():
    t1 = tasks.Task("one", 20)
    t2 = tasks.Task("two", 25)
    assert(t1.get_rate()) == 20
    assert(t2.get_name()) == "two"


def test_daily_plan_creation():
    t1 = tasks.Task("one", 20)
    t2 = tasks.Task("two", 25)
    d = tasks.DailyPlan()
    d.create_plan(t1, t2)
    assert(d.get_plan()) == [('one', 20), ('two', 25)]


def test_worker_creation():
    w1 = tasks.Worker("John")
    assert(w1.get_name()) == "John"


def test_tasks_assignment_from_daily_plan():
    t1 = tasks.Task("one", 20)
    t2 = tasks.Task("two", 25)
    d = tasks.DailyPlan()
    d.create_plan(t1, t2)
    w1 = tasks.Worker("John")
    w1.get_task_from_dp(d)
    assert(w1.get_current_task()) == ('two', 25)
    assert(d.get_plan()) == [('one', 20)]


def test_tasks_reporting():
    logg = tasks.Log()
    t1 = tasks.Task("one", 20)
    t2 = tasks.Task("two", 70)
    d = tasks.DailyPlan()
    d.create_plan(t1, t2)
    w1 = tasks.Worker("John")
    w2 = tasks.Worker("Mary")
    w2.get_task_from_dp(d)
    w2.log_task(logg, w2.get_current_task())
    w1.get_task_from_dp(d)
    w1.log_task(logg, w1.get_current_task(), 5)
    assert(logg.get_report()) == """Mary earned $70
John earned $100
"""
