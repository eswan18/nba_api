class API():
    def __init__(self, year=None, team=None):
        self.year = year
        self.team = team

    def get_playbyplay(self, year=None, team=None, season_segment=None):
        raise NotImplementedError
