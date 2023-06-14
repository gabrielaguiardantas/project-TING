"""https://www.youtube.com/watch?v=v6tALyc4C10
- Dica do Felps sobre importações no python"""

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    new_queue = {
        "nome_do_arquivo": str(path_file),
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    if new_queue not in instance.queue_list:
        print(new_queue)
        instance.enqueue(new_queue)


def remove(instance: Queue):
    if len(instance.queue_list) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    print(
        f"Arquivo {instance.queue_list[0]['nome_do_arquivo']}",
        "removido com sucesso",
        file=sys.stdout,
    )
    instance.dequeue()


def file_metadata(instance: Queue, position):
    if position < 0 or position > len(instance.queue_list) - 1:
        print("Posição inválida", file=sys.stderr)
        return
    print(instance.search(position))
