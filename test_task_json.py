import unittest
import numpy
from task import Task


class TestTaskJson(unittest.TestCase):
    def test_task_json(self):
        a = Task()
        txt = a.to_json()
        b = Task.from_json(txt)
        numpy.testing.assert_equal(a, b)


if __name__ == "__main__":
    unittest.main()
