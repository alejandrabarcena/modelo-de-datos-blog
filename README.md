# StarWars Blog – Modelo de Datos

Modelo en **SQLAlchemy** + diagrama **ER** para usuarios, personajes, planetas y favoritos.

## 🧱 Tech
- Python 3.13, SQLAlchemy
- ERAlchemy2 (genera `diagram.png`)
- PostgreSQL (DDL en `schema.sql`)
- ChartDB (diagrama online)

## ▶️ Reproducir el diagrama
```bash
pipenv install
pipenv run diagram   # genera diagram.png

📄 Estructura

src/models.py – modelos + serialize()

schema.sql – DDL PostgreSQL (importable en ChartDB → SQL Script)

diagram.png – diagrama generado desde código

🗺️ Diagrama

🔗 Diagrama interactivo (ChartDB)

Pega aquí tu link público de ChartDB


## Siguiente mini-paso (2 minutos)
1) Exporta desde ChartDB el **PNG/SVG** final y guárdalo como `diagram.png` en la raíz del repo (reemplaza el actual si quieres).  
2) Pega el README y sube:
```bash
git add README.md diagram.png
git commit -m "docs: README con diagrama y pasos de uso"
git push origin main

