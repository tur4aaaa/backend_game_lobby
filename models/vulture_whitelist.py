from models.game import Game
from models.player import Player
from models.team import Team
from models.lobby_manager import LobbyManager

def _vulture_keep():
    objects = [
        Game,
        Player,
        Team,
        LobbyManager,
    ]
    return objects

_vulture_keep()