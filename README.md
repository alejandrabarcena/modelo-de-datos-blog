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

# Mover el diagrama a la raíz si no está
mv src/diagram.png ./diagram.png

# Agregar y subir a GitHub
git add diagram.png README.md
git commit -m "docs: agregar diagrama al README"
git push origin main


