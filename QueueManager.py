from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManager(BaseManager):
    pass


task_queue = Queue()
result_queue = Queue()

QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)

if __name__ == "__main__":
    manager = QueueManager(address=("", 50000), authkey=b"secret")
    server = manager.get_server()
    print("[QueueManager] Server started.")
    server.serve_forever()
