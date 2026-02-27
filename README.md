# LinkedIn Automation con IA

Sistema de automatización para generar, evaluar y gestionar publicaciones técnicas en LinkedIn,
enfocado en contenido de desarrollador junior.

---

## 🎯 Objetivo
- Automatizar la generación de publicaciones técnicas.
- Usar IA para crear y evaluar contenido.
- Mantener control humano antes de publicar.
- Registrar métricas de calidad para mejora continua.

---

## 🧠 Arquitectura
config → selector → IA (generación) → IA (evaluación) → edición humana → listo/publicado

---

## 📁 Estructura

```txt
linkedin_automation/
├── ai/ # Generador y evaluador IA
├── core/ # Selector y pipeline
├── prompts/ # Prompts editables
├── data/ # CSVs (posts, historial)
├── main.py
```

---

## 🔄 Flujo de estados
- idea
- generado
- aprobado / rechazado
- editado
- listo
- publicado

---

## 🛡️ Manejo de errores
- Fallback si la IA no responde (cuota/límite).
- Evaluación robusta con JSON estricto.
- Pipeline no se rompe ante fallos externos.

---

## 🚀 Futuras mejoras
- Priorización por score histórico
- Métricas de engagement (likes, comentarios)
- UI simple para edición
- Programación de publicaciones