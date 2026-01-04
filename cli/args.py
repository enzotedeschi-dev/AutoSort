import argparse as arg
import logging

def config_args():
    parser = arg.ArgumentParser()

    parser.add_argument("--dir", type=str, help="Enter the path to scan.", required=True)
    parser.add_argument("--ext", nargs="*", default=None, help="Enter the file extensions to filter.")

    args = parser.parse_args()

    logging.info(
    "AutoSort started successfully. | dir=%s | ext=%s",
    args.dir,
    args.ext if args.ext else "No filter applied."
)

    return args