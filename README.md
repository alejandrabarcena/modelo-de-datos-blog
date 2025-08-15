# 🌌 Modelo de Datos - Blog Star Wars

Este proyecto es un **modelo de datos** para un blog interactivo sobre Star Wars.  
Usa **Python**, **SQLAlchemy** y **ERAlchemy** para definir la estructura de la base de datos y generar el diagrama UML.

---

## 📸 Diagrama UML

![ER Diagram](./diagram.png)

---

## 🚀 Tecnologías utilizadas

- 🐍 **Python 3**
- 🗄️ **SQLAlchemy** – ORM para definir y manejar las tablas
- 📊 **ERAlchemy2** – Generar diagramas UML desde el modelo
- 🐘 **PostgreSQL** – Base de datos recomendada
- 🌿 **Pipenv** – Gestión de entorno y dependencias
- 🖼 **Graphviz** – Renderizado de diagramas

---

## 📂 Estructura del proyecto

Modelo-de-Datos-del-blog/
│
├── src/
│ ├── models.py # Definición del modelo de datos con SQLAlchemy
│
├── diagram.png # Diagrama UML generado
├── Pipfile # Dependencias del proyecto
├── Pipfile.lock
└── README.md # Documentación del proyecto


---

## 🛠 Instalación y uso

1️⃣ **Clonar el repositorio**
```bash
git clone https://github.com/alejandrabarcena/modelo-de-datos-blog.git
cd modelo-de-datos-blog


2️⃣ Activar el entorno virtual con Pipenv

pipenv shell


3️⃣ Instalar dependencias

pipenv install


4️⃣ Generar el diagrama

pipenv run python src/models.py


Esto creará o actualizará el archivo diagram.png en la raíz del proyecto.

🧩 Modelo de datos
Tablas principales:

User – Información del usuario (email, password, nombre, apellido, etc.)

Planet – Información de planetas del universo Star Wars

Character – Información de personajes

FavoritePlanet – Relación de usuarios con sus planetas favoritos

FavoriteCharacter – Relación de usuarios con sus personajes favoritos

Relaciones:

Un usuario puede tener muchos planetas y personajes favoritos

Un planeta puede tener muchos fans (usuarios)

Un personaje puede tener muchos fans (usuarios)

Un personaje pertenece a un planeta (su planeta natal)

✨ Autor

Hecho con 💙 por Alejandra Barcena
