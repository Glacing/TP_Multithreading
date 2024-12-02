from QueueManager import QueueManager
from task import Task
import time
import queue
import threading


class Boss:
    def __init__(self, task_queue, result_queue):
        self.task_queue = task_queue
        self.result_queue = result_queue

    def create_tasks(self, number):
        task = Task(identifier=number)
        print(f"[Boss] Task {task.identifier} added to queue.")
        self.task_queue.put(task)

    def monitor_results(self):
        while True:
            try:
                result = self.result_queue.get(timeout=2)  # Attendre un résultat
                print(
                    f"[Boss] Task {result.identifier} completed in {result.time:.4f}s."
                )
            except queue.Empty:
                pass  # Pas de résultat pour l'instant


if __name__ == "__main__":
    QueueManager.register("get_task_queue")
    QueueManager.register("get_result_queue")
    manager = QueueManager(address=("localhost", 50000), authkey=b"secret")
    manager.connect()

    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()

    boss = Boss(task_queue, result_queue)

    result_thread = threading.Thread(target=boss.monitor_results, daemon=True)
    result_thread.start()

    i = 0
    while True:
        boss.create_tasks(i)
        i += 1
        time.sleep(1)
        ##boss.read_result_queue()
