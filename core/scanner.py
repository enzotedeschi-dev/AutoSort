from pathlib import Path
import logging
import shutil
from datetime import datetime
from ia.ia_dirscan import classifica_file_ai
from utils.report_manager.creazione_report import crea_report

class AutoSort:
    def __init__(self, percorso, ext):
        self.percorso = Path(percorso)
        self.ext = ext

        logging.info("AutoSort system configured and activated successfully...")

    def scansione(self):
        file_trovati = []

        if not self.percorso.exists():
            logging.error(f"The specified path ({self.percorso}) does not exist!")
            return None

        if not self.percorso.is_dir():
            logging.error("The specified path is not a directory!")
            return None
        
        for elemento in self.percorso.iterdir():
            if elemento.is_file():
                if self.ext is None:
                    logging.info(f"Item found: {elemento}")
                    file_trovati.append(elemento)
                else:
                    if elemento.suffix in self.ext:
                        logging.info(f"Item found: {elemento}")
                        file_trovati.append(elemento)
                    else:
                        logging.warning(f"The extension of the found file is not included among those specified: {elemento}. Skipping.")
            else:
                logging.warning(f"The found item is not a file: {elemento}. Skipping.")
        
        return file_trovati

    def analisi_cartelle(self):
        data_totale = {}

        while True:
            rimanenti = self.scansione()
            if not rimanenti:
                logging.info("No remaining files found. Classification completed.")
                break

            nomi_file = "\n".join(p.name for p in rimanenti)
            data = classifica_file_ai(nomi_file)

            file_spostati = 0
            for cartella, files in data.items():
                percorso_cartella = self.percorso / cartella
                percorso_cartella.mkdir(parents=True, exist_ok=True)
                logging.info(f"Folder '{cartella}' was created successfully.")

                for file in files:
                    origine = self.percorso / file
                    destinazione_file = percorso_cartella / origine.name

                    if not origine.exists():
                        logging.warning(f"Source file '{origine}' does not exist, skipping.")
                        continue

                    if destinazione_file.exists():
                        logging.warning(f"File '{destinazione_file.name}' already exists in folder '{cartella}'!")
                        continue

                    try:
                        shutil.move(origine, destinazione_file)
                        logging.info(f"File '{file}' was moved successfully to folder '{cartella}'!")
                        file_spostati += 1
                        data_totale.setdefault(cartella, []).append(file)
                    except Exception as e:
                        logging.error(f"Error while moving file '{file}' to folder '{cartella}': {e}")

            if file_spostati == 0:
                logging.warning("No files were moved in this iteration. Stopping to avoid an infinite loop.")
                break

        return data_totale
         
    def genera_report(self, data_json):
        file_totali = 0
        for lista in data_json.values():
            file_totali += len(lista)

        now = datetime.now()
        data_ora = now.strftime("%Y-%m-%d_%H:%M")

        report_dizionario = {
            "summary": {
                "date": data_ora,
                "total_files": file_totali,
                "folders_created": len(data_json),
            }
        }

        nome_file = crea_report(report_dizionario)
        logging.info(f"Report generated successfully: {nome_file}")