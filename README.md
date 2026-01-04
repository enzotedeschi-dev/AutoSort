# AutoSort

AutoSort scans a directory and organizes files into a small set of folders using an AI-based classification step.

This project is designed to be run locally (it **moves** files on your filesystem).

## Features

- **Directory scan** with optional extension filtering
- **AI classification** into a minimal set of general-purpose folders
- **Automatic folder creation** and file moving
- **JSON report** generation for each run
- **Structured logging** to console and `autosort.log`

> [!IMPORTANT]
> AutoSort uses AI to classify files. In rare cases, the AI may return an invalid response (e.g. JSON formatting issues) or an incomplete classification.
> If the program stops with an error or the result looks incomplete, run the same command again.
> AutoSort is designed with multiple safety filters/checks to reduce the impact of AI mistakes.
> Safety checks: no automatic renaming; unknown file names are skipped; existing destination files are skipped.

## Requirements

- Python 3.10+ (recommended)
- An OpenAI API key

## Installation

1. Create and activate a virtual environment.
2. Install dependencies.

```bash
python -m pip install -r requirements.txt
```

## Configuration

### OpenAI API key (`OPENAI_API_KEY`)

Create a `.env` file in the project root (you can copy `.env.example`) and set:

- `OPENAI_API_KEY=...`

Do **not** commit your `.env` file.

Alternatively, you can set `OPENAI_API_KEY` as an environment variable.

## Usage

Example (Windows path shown):

```bash
python main.py --dir "C:\\Users\\youruser\\Downloads" --ext .png .jpg
```

- `--dir` is required
- `--ext` is optional (if omitted, no extension filtering is applied)

## Safety notes

- This tool **moves files**. Test on a copy or on a dedicated folder first.
- If a destination file already exists, AutoSort will skip moving that file.

## Project structure

```text
AutoSort/
  main.py
  core/
    scanner.py
  cli/
    args.py
  ia/
    ia_dirscan.py
  utils/
    logging_setup.py
    json/
      parse_json.py
    report_manager/
      creazione_report.py
```

## Troubleshooting

- **Missing OPENAI_API_KEY**
  - Create a `.env` file (see `.env.example`) or set the `OPENAI_API_KEY` environment variable.
- **The AI output is not valid JSON**
  - The tool expects the model response to be JSON-only. If it fails, retry.
