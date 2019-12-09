"""
tests file
"""
import tasks


def test_report_hourly():
    """

    :return:
    """
    w1 = tasks.Log("Bill", 'Task1')
    assert w1.report() == "Please pay 50$ to Bill for Task1!"


def test_report_fixed():
    """

    :return:
    """
    w2 = tasks.Log("Ted", 'Task3')
    assert w2.report() == "Please pay 500$ to Ted for Task3!"


def test_report_none():
    """

    :return:
    """
    w2 = tasks.Log("Tony", 'Task4')
    assert w2.report() == "Worker or Task doesnt exists"
