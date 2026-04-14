# backend_game_lobby
# 🎮 Game Lobby Backend System

A backend project for a multiplayer game lobby system built with Python and PostgreSQL.

This project simulates a basic game infrastructure where players can be created, stored in a database, and later extended into lobbies, teams, and full game sessions.

---

## 🚀 Features

- 👤 Player system (create & fetch players)
- 🗄️ PostgreSQL database integration
- 🧠 Clean project structure (models / database / utils)
- ⚙️ Main entry point for testing logic (main.py)
- 🔧 Ready for extension (lobby, game, teams systems)

---

## 🧱 Project Structure
Game_lobby/
│
├── database/
│ ├── db.py # Database connection & queries
│ └── database.sql # SQL schema
│
├── models/
│ └── (game logic models)
│
├── utils/
│ └── (helper functions - future use)
│
└── main.py # Entry point for testing

---

## 🛠️ Tech Stack

- Python 🐍
- PostgreSQL 🐘
- psycopg2

---

## ⚙️ Setup & Run

### 1. Install dependencies
```bash
pip install psycopg2
```

2. Create database

Run SQL from database/database.sql in PostgreSQL.

3. Configure connection
Update credentials in db.py:
host="localhost"
database="game_db"
user="postgres"
password="your_password"

4. Run project:
python main.py

 Future Improvements
 Lobby system (create / join / leave)
 Teams system
 Game session logic
 REST API (FastAPI integration)
 Environment variables (.env support)
