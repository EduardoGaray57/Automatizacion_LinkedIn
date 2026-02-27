import os
from openai import OpenAI

_client = None

def get_client():
    global _client

    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise Exception("OPENAI_API_KEY no definida")
        
        _client = OpenAI(api_key=api_key)

    return _client