"""
    This module provides us with a drainable multiprocess aware message queue.

"""

from multiprocessing import Event, Queue
from multiprocessing.managers import BaseManager
from queue import Empty
from typing import Any, List

from .debugging import app_logger as log


class QueueWrapper(object):
    def __init__(self, name: str, q: Queue = None, prevent_writes: Event = None):
        self.name = name
        self.q: Queue = q or Queue()
        self._prevent_writes: Event = prevent_writes or Event()

    def get(self) -> Any:
        """
        This call blocks unit it gets a messge from the queue.
        if the queue is drained, it returns the sentinel string STOP
        if the queue is closed while this call is blocking, it'll return STOP
        """
        if self.is_drained:
            return "STOP"

        try:
            return self.q.get()
        except Exception as ex:
            log.info(f"q.get() failed with {ex}")
            return "STOP"

    def put(self, obj: object):
        if self.is_writable:
            log.debug(f"putting {obj} on queue {self.name}")
            self.q.put(obj)

    def put_many(self, objs: List[object]):
        for obj in objs:
            self.put(obj)

    def prevent_writes(self):
        """prevent external writes to the queue"""
        log.info(f"preventing writes to queue {self.name}")
        self._prevent_writes.set()

    @property
    def is_writable(self) -> bool:
        return not self._prevent_writes.is_set()

    @property
    def is_drained(self) -> bool:
        return not self.is_writable and self.empty

    @property
    def empty(self) -> bool:
        return self.q.empty()


class QueueManager(BaseManager):
    pass


def register_manager(name: str, queue: QueueWrapper = None):
    if queue:
        QueueManager.register(name, callable=lambda: queue)
    else:
        QueueManager.register(name)


def create_queue_manager(port: int) -> QueueManager:
    return QueueManager(address=("127.0.0.1", port), authke=b"ingestbackend")
