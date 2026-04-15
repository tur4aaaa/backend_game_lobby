import asyncio

from team import Team


class Game:
    def __init__(
        self,
        teams,
    ):
        self.teams = teams
        self.players = []

        for team in teams:
            self.players.extend(team.players)

        self.game_running = False
        self.current_tick = 0
        self.max_ticks = 10

    async def start(self):
        if self.game_running:
            print("Game already running")
            return

        self.game_running = True
        print("Game started")

        asyncio.create_task(self.game_loop)

    async def game_loop(self):
        while self.game_running:

            self.process_actions()
            self.current_tick += 1

            print(f"tick: {self.current_tick}")

            if self.current_tick >= self.max_ticks:
                await self.stop()
                break

            await asyncio.sleep(1)

    def process_actions(self):
        for team in self.teams:
            for player in team.players:
                if player.status == "ready":
                    team.score += 1
                elif player.status == "damaged":
                    team.score += 0

    async def update_scores(self):
        pass

    def check_winner(self):
        biggest_score = self.teams[0]
        for team in self.teams:
            if team.score > biggest_score.score:
                biggest_score = team

        print(f"This team has the biggest score :{biggest_score}")
        return biggest_score

    async def stop(self):
        if self.game_running:
            self.game_running = False
            print("Game stopped")
            self.check_winner()
        else:
            print("Game is already stopped")
