import argparse as arg
import logging

def config_args():
    parser = arg.ArgumentParser()

    parser.add_argument("--dir", type=str, help="Enter the path to scan.", required=True)
    parser.add_argument("--ext", nargs="*", default=None, help="Enter the file extensions to filter.")

    args = parser.parse_args()

    if args.ext:
        args.ext = [e.lower() if e.startswith(".") else f".{e.lower()}" for e in args.ext]

    logging.info(
    "AutoSort started successfully. | dir=%s | ext=%s",
    args.dir,
    args.ext if args.ext else "No filter applied."
)

    return args