# 🎮 Backend Game Lobby

A backend project for a game lobby system.

The project is written in Python and uses PostgreSQL as the database.

---

## ⚙️ Tech Stack

- Python
- PostgreSQL
- Git / GitHub
- JWT (JSON Web Tokens) for authentication

---

## 📁 Project Structure
src/
main.py # application entry point
models/ # database models
database/ # PostgreSQL connection and setup

---

## 🗄️ Database (PostgreSQL)

The project uses PostgreSQL for data storage.

It stores:

- users
- game lobbies
- game state

Database connection logic is located in `src/database/`.

---

## 🚀 How to Run

1. Install dependencies:
```bash `
poetry install -r requirements.txt
Configure PostgreSQL database
Run the application:
python src/main.py


🧠 Project Description

This backend system is designed for a game lobby where users can:

create lobbies
join games
manage player state
store data in PostgreSQ
