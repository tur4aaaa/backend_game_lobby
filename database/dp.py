import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="game_db",
        user="postgres",
        password="turgay2727",
        DB_PORT = 5432,
    )
    return conn


def get_player(player_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("Select * FROM PLAYERS WHERE id = %s", (player_id,))
    player = cur.fetchone()

    cur.close()
    conn.close()

    return player


def create_player(name):
    conn = get_connection()
    cur = conn.cursor()

    query = (
        "INSERT INTO Players (name, player_state, statistic) "
        "VALUES (%s, %s, %s)"
    )

    cur.execute(
        query,
        (name, "offline", "{}"),
    )

    conn.commit()
    cur.close()
    conn.close()