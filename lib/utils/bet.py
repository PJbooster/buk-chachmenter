class Bet:
    def __init__(self, team_1: str, team_2: str, odds_team1: str, odds_team2: str):
        self._team_1 = team_1
        self._team_2 = team_2
        self.odds_team1 = float(odds_team1)
        self.odds_team2 = float(odds_team2)

    @property
    def team_1(self) -> str:
        return self._team_1

    @property
    def team_2(self) -> str:
        return self._team_2

    @property
    def odds_team1(self) -> float:
        return self.odds_team1

    @property
    def odds_team2(self) -> float:
        return self.odds_team2
