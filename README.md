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

Review
---
- flake8 database/ main.py models/ выдаёт много всего, это стоит пофиксить
- в проекте вроде поетри, а в доке pip install?
- пайплайн с линтерами должен быть зелёный)
- питон 3.11 уже можно спокойно заменять на 3.14
- print в продакшен коде не используется
- в целом не очень понятен смысл этой репы и что за проект и зачем?
- весь код проекта лучше положить в отдельную папку, типа src или app
- рядом должна быть папка с тестами
- тесты, соответственно, тоже нужны)
- и в пайплайне чтобы запускались сами
- тайпинг в коде питона нужен
- `form_teams` - можно использовать готовую функцию batched для формирования команд
- `dp.py` - with поможет закрывать коннекты к пг и избавит от бойлерплейт кода
- `Game.__init__` - конструктор списка просится для players
- `change_status` - нужен Enum над статусами
- `update_score` - sum([...]) будет приятнее смотреться вместо списка с +=
