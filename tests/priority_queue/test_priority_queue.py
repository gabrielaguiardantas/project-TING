from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    new_queue_list = PriorityQueue()

    new_queue_priority_el1 = {
        "nome_do_arquivo": "str(path_file)",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["a", "b", "c", "d"],
    }
    new_queue_priority_el2 = {
        "nome_do_arquivo": "str(path_file)",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ["a", "b"],
    }
    new_queue_no_priority_el = {
        "nome_do_arquivo": "str(path_file)",
        "qtd_linhas": 7,
        "linhas_do_arquivo": ["a", "b", "c", "d", "8", "awsda", "sdsdvc"],
    }
    new_queue_list.enqueue(new_queue_priority_el1)
    assert len(new_queue_list) == 1

    new_queue_list.dequeue()
    assert len(new_queue_list) == 0

    new_queue_list.enqueue(new_queue_priority_el1)
    with pytest.raises(IndexError):
        new_queue_list.search(4)

    assert len(new_queue_list.regular_priority) == 0

    assert new_queue_list.is_priority(new_queue_priority_el1) is True

    new_queue_list.enqueue(new_queue_no_priority_el)
    new_queue_list.enqueue(new_queue_priority_el2)

    assert new_queue_list.search(2) == new_queue_no_priority_el
