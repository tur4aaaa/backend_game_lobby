import asyncio
import random
import logging

from models.team import Team


class LobbyManager:

    def __init__(self):
        self.players = []
        self.teams = []
        self.game_started = False

    def add_player(self, player):
        # Добавляет игрока если он не в лобби
        if player not in self.players:
            self.players.append(player)

    def remove_player(self, player):
        # Удаляем игрока если он в лобби
        if player in self.players:
            self.players.remove(player)

    def form_teams(self, team_size=5):
        random.shuffle(self.players)
        self.teams = []
        team_number = 1
        for i in range(0, len(self.players), team_size):
            team_players = self.players[i:i + team_size]

            team = Team(
                team_name=f"Team {team_number}",
                players=team_players,
                score=0,
            )
            self.teams.append(team)

            team_number += 1

    def all_ready(self):
        for player in self.players:
            if player.status != "ready":
                return False
        return True

    async def start_game(self):
        if self.game_started:
            logging.info("Game is on process")
            return

        check_game_status = self.all_ready()
        if not check_game_status:
            logging.info("Someone from players is not ready yet")
            return

        self.form_teams()

        self.game_started = True
        logging.info("Game started")

        asyncio.create_task(self.game_tick())

    async def game_tick(self):
        while self.game_started:
            for team in self.teams:
                team.update_score()
            for team in self.teams:
                damaged, active = team.player_status()
                logging.info(
                    f"{team.team_name}: active = {len(active)},damaged = {len(damaged)}"
                )

            await asyncio.sleep(1)
