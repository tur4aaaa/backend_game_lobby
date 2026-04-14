from team import Team


class Player:

    def __init__(self, name, score, status, team):
        self.name = name
        self.score = score
        self.status = status
        self.team = team

    def join_team(self, team):
        if self.team is not None:
            self.leave_team(self.team)
        if self not in team.players:
            team.players.append(self)
        self.team = team

    def leave_team(self, team):
        if self in team.players:
            team.players.remove(self)
            self.team = None

    def change_status(self, status):
        if status in ["online", "offline", "ready", "damaged"]:
            self.status = status
            print(f"{self.name} status changed to {self.status}")

    def get_info(self):
        result = {
            "name": self.name,
            "status": self.status,
            "score": self.score,
            "team": self.team.team_name if self.team is not None else None,
        }
        return result
