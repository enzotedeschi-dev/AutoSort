import json 
import logging
from pathlib import Path

config_structure = {
    "openai-model": "gpt-4o-mini",
    "temperature": 0
}

PERCORSO_CONFIG = Path("config.json")

def crea_config():
    with open(PERCORSO_CONFIG, "w", encoding="utf-8") as file:
        json.dump(config_structure, file, indent=4, ensure_ascii=False)
    logging.info(f"Created default config file: {PERCORSO_CONFIG}")

def carica_config():
    with open(PERCORSO_CONFIG, "r", encoding="utf-8") as file:
        config_dict = json.load(file)
    logging.info(f"Loaded config file: {PERCORSO_CONFIG}")
    return config_dict

def initialize_config():
    #Crea il config se non esiste
    if not PERCORSO_CONFIG.exists():
        crea_config()

    #Carica il config
    config_data = carica_config()
    return config_data