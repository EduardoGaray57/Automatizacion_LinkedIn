from pathlib import Path
from ai.client import get_client
import openai
import json

PROMPT_FILE = Path("prompts/evaluar_post.txt")


def cargar_prompt():
    return PROMPT_FILE.read_text(encoding="utf-8")


def evaluar_post(contenido):
    prompt = cargar_prompt().format(contenido=contenido)

    try:
        client = get_client()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un revisor de contenido técnico para LinkedIn."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=120
        )

        raw = response.choices[0].message.content.strip()
        resultado = json.loads(raw)

        return resultado

    except (openai.RateLimitError, json.JSONDecodeError):
        # 🔹 Fallback seguro
        return {
            "score": 0.5,
            "decision": "aprobado",
            "feedback": "Evaluación automática no disponible, revisar manualmente."
        }