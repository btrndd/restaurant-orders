import csv
import os


def analyze_log(path_to_file):
    if(path_to_file[-3:] != "csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    if not os.path.exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open(path_to_file, encoding="utf8") as file:
        report_reader = csv.reader(file, delimiter=",")
        list_result = {
            f"{index}": (row[0], row[1], row[2])
            for index, row in enumerate(report_reader)
        }

    orders = {
        "maria": {
            "hamburguer": 0, "coxinha": 0, "pizza": 0, "misto-quente": 0
        },
        "arnaldo": {
            "hamburguer": 0, "coxinha": 0, "pizza": 0, "misto-quente": 0
        },
        "joao": {
            "hamburguer": 0, "coxinha": 0, "pizza": 0, "misto-quente": 0
        },
        "jose": {
            "hamburguer": 0, "coxinha": 0, "pizza": 0, "misto-quente": 0
        },
    }

    for order in list_result.values():
        orders[order[0]][order[1]] += 1

    results = list()
    # Qual o prato mais pedido por 'maria'?
    results.append(max(orders["maria"], key=orders["maria"].get))
    # Quantas vezes 'arnaldo' pediu 'hamburguer'?
    results.append(orders["arnaldo"]["hamburguer"])

    joao_result = joao_infos(orders, list_result)
    results.append(joao_result[0])
    results.append(joao_result[1])

    write_txt(results)


def joao_infos(orders, list_result):
    result = list()
    # Quais pratos 'joao' nunca pediu?
    joao_never_asked = set()
    for plate in orders["joao"]:
        if orders["joao"][plate] == 0:
            joao_never_asked.add(plate)
    result.append(joao_never_asked)

    # Quais dias 'joao' nunca foi à lanchonete?
    days = {order[2] for order in list_result.values()}
    joao_days = set()
    for order in list_result.values():
        if order[0] == "joao":
            joao_days.add(order[2])
    result.append(days.difference(joao_days))
    return result


def write_txt(results):
    with open("data/mkt_campaign.txt", "w") as file:
        for index, result in enumerate(results):
            if index == 0:
                file.write(result)
            else:
                file.write(f"\n{result}")


if __name__ == '__main__':
    analyze_log("data/orders_1.csv")
