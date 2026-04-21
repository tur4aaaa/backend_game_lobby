from flask import Flask, request, jsonify
from src.auth.auth_routes import auth_bp
from src.auth.auth_middleware import auth_required
from src.models.lobby_manager import LobbyManager

app = Flask(__name__)


app.register_blueprint(auth_bp)

lobby = LobbyManager()


@app.route("/")
def home():
    return {"message": "Game lobby server is running"}



@app.route("/lobby/join", methods=["POST"])
@auth_required
def join_lobby():
   
    user_id = request.user_id

    
    from models.player import Player

    player = Player(
        name=str(user_id),
        score=0,
        status="online",
        team=None
    )

    lobby.add_player(player)

    return jsonify({
        "message": "joined",
        "player": player.get_info()
    })



@app.route("/lobby/start", methods=["POST"])
@auth_required
def start_game():
    import asyncio

    # аккуратно запускаем игру
    asyncio.create_task(lobby.start_game())

    return jsonify({"message": "game started"})


if __name__ == "__main__":
    app.run(debug=True)