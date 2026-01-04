import json 
from datetime import datetime 

def crea_report(dizionario):
    data_ora = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    nome_file = f"report_{data_ora}.json"

    with open(nome_file, "w", encoding="utf-8") as file:
        json.dump(dizionario, file, indent=4, ensure_ascii=False)

    return nome_file