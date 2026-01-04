import logging
from utils.logging_setup import setup_logging
from core.scanner import AutoSort
from cli.args import config_args

def main():
    setup_logging()
    args = config_args()

    logging.info("Initializing AutoSort script...")

    scanner = AutoSort(args.dir, args.ext)

    logging.info("Starting intelligent scan...")
    risultati = scanner.scansione()

    if risultati is not None:
        logging.info("Starting classification via the artificial intelligence algorithm...")
        data_json = scanner.analisi_cartelle()
        scanner.genera_report(data_json)
    else:
        logging.critical("Classification process stopped due to scan errors!")


if __name__ == "__main__":
    main()