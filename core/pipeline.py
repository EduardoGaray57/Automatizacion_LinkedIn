import csv
from datetime import datetime
from core.selector import seleccionar_idea
from ai.generator import generar_post
from ai.evaluator import evaluar_post

POSTS_FILE = "data/posts.csv"

def inicializar_posts():
    try:
        with open(POSTS_FILE, "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        with open(POSTS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "fecha",
                "categoria",
                "tipo",
                "tema",
                "contenido",
                "estado",
                "score",
                "feedback"
            ])

def registrar_post_generado(idea, contenido):
    with open(POSTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            idea["categoria"],
            idea["tipo"],
            idea["tema"],
            contenido,
            "generado"
        ])

def ejecutar_pipeline():
    inicializar_posts()

    idea = seleccionar_idea()
    contenido = generar_post(idea)
    evaluacion = evaluar_post(contenido)

    estado = "aprobado" if evaluacion["decision"] == "aprobado" else "rechazado"

    with open(POSTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            idea["categoria"],
            idea["tipo"],
            idea["tema"],
            contenido,
            estado,
            evaluacion.get("score"),
            evaluacion.get("feedback")
        ])

    print("🧠 Evaluación IA:", evaluacion)
    print("📌 Estado final:", estado)