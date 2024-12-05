import time
import json

import numpy as np


class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = size or np.random.randint(300, 3_000)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self):
        jsonValue = {"a": self.a.tolist(), "b": self.b.tolist()}
        return json.dumps(jsonValue)

    @classmethod
    def from_json(text: str):
        dictValue = json.loads(text)
        newTask = Task()
        newTask.a = dictValue["a"]
        newTask.b = dictValue["b"]
        return newTask

    def __eq__(self, other: "Task"):
        return self.a == other.a and self.b == other.b
