from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue_list = []

    def __len__(self):
        return len(self.queue_list)

    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        return self.queue_list.pop(0)

    def search(self, index):
        if index < 0 or index > len(self.queue_list) - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue_list[index]
