import json
import csv
import random
from collections import defaultdict

CONFIG_FILE = "config/config_posts.json"
HISTORIAL_FILE = "data/historial.csv"

def cargar_config():
    try:
        with open(CONFIG_FILE, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise Exception(
            f"El archivo {CONFIG_FILE} no contiene un JSON valido"
        )

def cargar_historial():
    usados = set()
    try:
        with open(HISTORIAL_FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 3:
                    usados.add((row[1], row[2], row[3]))
    except FileNotFoundError:
        pass
    return usados

def cargar_scores():
    """
    Devuelve score promedio por (categoria, tipo)
    """
    scores = defaultdict(list)

    try:
        with open("data/posts.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("score"):
                    key = (row["categoria"], row["tipo"])
                    scores[key].append(float(row["score"]))
    except FileNotFoundError:
        pass

    promedios = {
        k: sum(v) / len(v)
        for k, v in scores.items()
    }

    return promedios

def seleccionar_idea():
    config = cargar_config()
    categorias = config["categorias"]
    tipos = config["tipos_post"]

    usados = cargar_historial()
    scores = cargar_scores()

    ideas = []

    for categoria, temas in categorias.items():
        for tipo in tipos:
            for tema in temas:
                if (categoria, tipo, tema) in usados:
                    continue

                peso = scores.get((categoria, tipo), 0.5)

                ideas.append({
                    "categoria": categoria,
                    "tipo": tipo,
                    "tema": tema,
                    "peso": peso
                })

    if not ideas:
        raise Exception("No hay ideas nuevas disponibles")

    # 70% basado en score, 30% random
    if random.random() < 0.7:
        total = sum(i["peso"] for i in ideas)
        r = random.uniform(0, total)
        acumulado = 0
        for idea in ideas:
            acumulado += idea["peso"]
            if acumulado >= r:
                return idea
    else:
        return random.choice(ideas)