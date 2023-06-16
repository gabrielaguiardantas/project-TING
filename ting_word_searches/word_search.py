def exists_word(word, instance):
    search_list = []
    for queue in instance.queue_list:
        for line in queue["linhas_do_arquivo"]:
            line_converted = line.casefold()
            word_converted = word.casefold()
            if word_converted in line_converted:
                if (
                    len(search_list) != 0
                    and queue["nome_do_arquivo"] == search_list[-1]["arquivo"]
                ):
                    search_list[-1]["ocorrencias"].append(
                        {"linha": queue["linhas_do_arquivo"].index(line) + 1}
                    )
                else:
                    search_list.append(
                        {
                            "palavra": word,
                            "arquivo": queue["nome_do_arquivo"],
                            "ocorrencias": [
                                {
                                    "linha": queue["linhas_do_arquivo"].index(
                                        line
                                    )
                                    + 1
                                }
                            ],
                        }
                    )
    return search_list


def search_by_word(word, instance):
    new_search = exists_word(word, instance)
    for el in new_search:
        for oc in el["ocorrencias"]:
            oc["conteudo"] = instance.queue_list[new_search.index(el)][
                "linhas_do_arquivo"
            ][oc["linha"] - 1]
    return new_search
