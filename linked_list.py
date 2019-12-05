"""linked list realisation"""


class Item:
    """Item realisation"""
    def __init__(self,  worker_name, task_name, task_payment):
        self._worker_name = worker_name
        self._task_name = task_name
        self._task_payment = task_payment
        self.next = None
        self.previous = None

    def __repr__(self):
        return self._worker_name

    def worker_name(self):
        """return worker name"""
        return self._worker_name

    def task_name(self):
        """return task name"""
        return self._task_name

    def task_payment(self):
        """return task payment"""
        return self._task_payment

class List:
    """item list realisation"""
    def __init__(self):
        self.head = None

    def state(self):
        """
        :return: items list in str format
        """
        result = []
        if self.head is not None:
            current = self.head
            result = [current]
            while current.previous is not None:
                current = current.previous
                result.append(current)
            return result
        return result

    def insert(self, worker_name, task_name, task_payment):
        """
        Insert item in list
        :return: None
        """
        if self.head is None:
            self.head = Item(worker_name, task_name, task_payment)
        else:
            new = Item(worker_name, task_name, task_payment)
            new.previous = self.head
            self.head.next = self.head = new


    def delete(self):
        """
        Delete item from list
        :return: deleted item
        """
        if self.head is not None:
            for_del = self.head
            self.head = self.head.previous
            self.head.next = None
            return for_del
        raise IndexError
