from player import Player
class Team:
    
    def __init__(self,team_name,players,score):
        self.team_name = team_name
        self.players = players
        self.score = score

    def player_status(self):
        damaged_players = []
        active_players = []
        for player in self.players:
            if player.status == "Damaged":
                damaged_players.append(player)
            else:
                active_players.append(player)
        return damaged_players,active_players
    
  
    def update_score(self):
        total = 0
        for player in self.players:
            total += player.score
        self.score = total

    def get_team_info(self):
        self.update_score()
        team_info = {
            "team_name":self.team_name,
            "score":self.score,
            "players": [player.get_info() for player in self.players]
        }
        return team_info