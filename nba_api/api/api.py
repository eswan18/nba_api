class API():
    def __init__(self, year=None, team=None):
        self.year = year
        self.team = team

    def get_playbyplay(self, team=None, year=None, season_segment=None):
        team_id = self._resolve_team_ref(team)
        season_id = self._fmt_year_as_season(year)

    def _resolve_team_ref(self, team_str):
        return NotImplemented

    def _fmt_year_as_season_id(self, year):
        year = str(year)
        return year + str(int(year + 1))[:2]

    def get_game_info(self):
        return NotImplemented

    def _get_event_msg_type_desc(self, event_msg_type):
        return NotImplemented

    def get_box_scores(self):
        return NotImplemented
