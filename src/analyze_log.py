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

    # Qual o prato mais pedido por 'maria'?
    maria_plate = max(orders["maria"], key=orders["maria"].get)
    # Quantas vezes 'arnaldo' pediu 'hamburguer'?
    arnaldo_qty_burger = orders["arnaldo"]["hamburguer"]
    # Quais pratos 'joao' nunca pediu?
    joao_never_asked = set()
    for index, plate in enumerate(orders["joao"]):
        if orders["joao"][plate] == 0:
            joao_never_asked.add(plate)
    # Quais dias 'joao' nunca foi à lanchonete?
    days = {order[2] for order in list_result.values()}
    joao_days = set()
    for order in list_result.values():
        if order[0] == "joao":
            joao_days.add(order[2])
    joao_not_days = days.difference(joao_days)
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(maria_plate)
        file.write(f"\n{arnaldo_qty_burger}")
        file.write(f"\n{joao_never_asked}")
        file.write(f"\n{joao_not_days}")


if __name__ == '__main__':
    analyze_log("data/orders_1.csv")