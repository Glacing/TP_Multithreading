from QueueManager import QueueClient
from task import Task
import time
import queue
import threading


class Boss:
    def __init__(self, task_queue, result_queue):
        self.task_queue = task_queue
        self.result_queue = result_queue

    def create_tasks(self, number):
        task = Task(number, 1000)
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
    client = QueueClient()
    boss = Boss(client.task_queue, client.result_queue)

    result_thread = threading.Thread(target=boss.monitor_results, daemon=True)
    result_thread.start()

    i = 0
    while True:
        boss.create_tasks(i)
        i += 1
        time.sleep(1)
        ##boss.read_result_queue()
