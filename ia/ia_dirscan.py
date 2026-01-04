import os
from utils.json.parse_json import json_from_model
from dotenv import load_dotenv
from openai import OpenAI
from utils.config.load_config import initialize_config

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def classifica_file_ai(prompt: str) -> dict:
    config = initialize_config()
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY. Create a .env file (see .env.example) or set the environment variable before running.")

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=config["openai-model"],
        temperature=config["temperature"],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "folder_map",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                }
            }
        },
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that helps organize files on a PC. "
                    "You are given only the file names, one per line. "
                    "Use ONLY the provided file names. Do not invent file names and do not rename them. "
                    "You must group the files into as few general categories as possible, using the smallest possible number of folders. "
                    "Remember to choose folder names based on the file names and extensions. "
                    "If appropriate, be specific when creating folders so the user can easily find files. "
                    "Folder names should start with a capital letter."
                )
            },
            {"role": "user", "content": prompt},
        ],
    )

    risposta = response.choices[0].message.content
    data = json_from_model(risposta)

    return data