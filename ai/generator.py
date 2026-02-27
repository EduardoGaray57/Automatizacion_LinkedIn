from pathlib import Path
from ai.client import get_client
import openai

PROMPT_FILE = Path("prompts/generar_post.txt")

def cargar_prompt():
    return PROMPT_FILE.read_text(encoding="utf-8")

def generar_post(idea):
    prompt = cargar_prompt().format(
        categoria=idea["categoria"],
        tipo=idea["tipo"],
        tema=idea["tema"]
    )
    try:
        client = get_client()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un desarrollador de software junior."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=180
        )
        return response.choices[0].message.content.strip()
    except openai.RateLimitError:
        # 🔹 Fallback seguro (MOCK)
        return (
            f"Cuando estaba aprendiendo sobre {idea['tema']}, "
            f"me di cuenta de que aplicar buenas prácticas desde el inicio "
            f"marca una gran diferencia en el desarrollo. "
            f"Aunque al principio cuesta, con el tiempo se vuelve clave. "
            f"¿Te pasó algo parecido?"
        )