from QueueManager import QueueManager
import time
import queue


class Minion:
    def __init__(self, task_queue, result_queue, name):
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.name = name

    def work(self):
        while True:
            try:
                task = self.task_queue.get(timeout=2)
                print(f"[{self.name}] Working on Task {task.identifier}...")
                task.work()
                print(f"[{self.name}] Task {task.identifier} done in {task.time:.4f}s.")
                self.result_queue.put(task)
            except queue.Empty:
                print(f"[{self.name}] No tasks available, waiting...")
                time.sleep(1)


if __name__ == "__main__":
    QueueManager.register("get_task_queue")
    QueueManager.register("get_result_queue")
    manager = QueueManager(address=("localhost", 50000), authkey=b"secret")
    manager.connect()

    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()

    minion = Minion(task_queue, result_queue, "Minion-1")
    minion.work()
