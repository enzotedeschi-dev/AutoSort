import os
from utils.json.parse_json import parse_json_from_model
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def classifica_file_ai(prompt: str) -> dict:
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY. Create a .env file (see .env.example) or set the environment variable before running.")

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that helps organize files on a PC. "
                    "You are given only the file names, one per line. "
                    "You must group the files into as few general categories as possible, using the smallest possible number of folders. "
                    "Remember to choose folder names based on the file names and extensions. "
                    "If appropriate, be specific when creating folders so the user can easily find files. "
                    "You must return the response exclusively in JSON format. "
                    "Each JSON property key must be a folder name (with the first letter capitalized), and the value must be a list of file names that should be placed in that folder. "
                    "Do not add any text outside the JSON, nor comments, nor explanations."
                )
            },
            {"role": "user", "content": prompt},
        ],
    )

    risposta = response.choices[0].message.content
    data = parse_json_from_model(risposta)
    
    return data