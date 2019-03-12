import re
from nba_api.stats.library.data import teams
from nba_api.stats.library.data import team_index_id, team_index_abbreviation, team_index_nickname, team_index_full_name
from nba_api.stats.library.data import team_index_city, team_index_state, team_index_year_founded


def _find_teams(regex_pattern, row_id):
    teams_found = []
    for team in teams:
        if re.search(regex_pattern, str(team[row_id]), flags=re.I):
            teams_found.append(_get_team_dict(team))
    return teams_found


def _get_team_dict(team_row):
    return {
        'id': team_row[team_index_id],
        'full_name': team_row[team_index_full_name],
        'abbreviation': team_row[team_index_abbreviation],
        'nickname': team_row[team_index_nickname],
        'city': team_row[team_index_city],
        'state': team_row[team_index_state],
        'year_founded': team_row[team_index_year_founded]
    }


def find_teams_by_full_name(regex_pattern):
    return _find_teams(regex_pattern, team_index_full_name)


def find_teams_by_state(regex_pattern):
    return _find_teams(regex_pattern, team_index_state)


def find_teams_by_city(regex_pattern):
    return _find_teams(regex_pattern, team_index_city)


def find_teams_by_nickname(regex_pattern):
    return _find_teams(regex_pattern, team_index_nickname)


def find_teams_by_year_founded(year):
    teams_found = []
    for team in teams:
        if team[team_index_year_founded] == year:
            teams_found.append(_get_team_dict(team))
    return teams_found


def find_team_by_abbreviation(abbreviation):
    regex_pattern = '^{}$'.format(abbreviation)
    teams_list = _find_teams(regex_pattern, team_index_abbreviation)
    if len(teams_list) > 1:
        raise Exception('Found more than 1 id')
    elif not teams_list:
        return None
    else:
        return teams_list[0]


def find_team_name_by_id(team_id):
    regex_pattern = '^{}$'.format(team_id)
    teams_list = _find_teams(regex_pattern, team_index_id)
    if len(teams_list) > 1:
        raise Exception('Found more than 1 id')
    elif not teams_list:
        return None
    else:
        return teams_list[0]


def get_teams():
    teams_list = []
    for team in teams:
        teams_list.append(_get_team_dict(team))
    return teams_list

def _team_abb_list():
    return ['ATL','BOS','CLE','NOP','CHI','DAL','DEN',
            'GSW','HOU','LAC','LAL','MIA','MIL','MIN',
            'BKN','NYK','ORL','IND','PHI','PHX','POR',
            'SAC','SAS','OKC','TOR','UTA','MEM','WAS','DET','CHA']

def _team_full_name_list():
    return ['Atlanta Hawks','Boston Celtics','Cleveland Cavaliers','New Orleans Pelicans',
            'Chicago Bulls','Dallas Mavericks','Denver Nuggets','Golden State Warriors','Houston Rockets',
            'Los Angeles Clippers','Los Angeles Lakers','Miami Heat','Milwaukee Bucks','Minnesota Timberwolves',
            'Brooklyn Nets','New York Knicks','Orlando Magic','Indiana Pacers','Philadelphia 76ers','Phoenix Suns',
            'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs','Oklahoma City Thunder',
            'Toronto Raptors','Utah Jazz','Memphis Grizzlies','Washington Wizards','Detroit Pistons','Charlotte Hornets']

def _team_city_list():
    return ['Atlanta','Boston','Cleveland','New Orleans','Chicago',
            'Dallas','Denver','Golden State','Houston','Los Angeles',
            'Miami','Milwaukee','Minnesota','Brooklyn','New York','Orlando',
            'Indiana','Philadelphia','Phoenix','Portland','Sacramento','San Antonio',
            'Oklahoma City','Toronto','Utah','Memphis','Washington','Detroit','Charlotte']

def _team_id_list():
    return ['1610612737','1610612738','1610612739','1610612740','1610612741','1610612742','1610612743', '1610612744',
            '1610612745','1610612746','1610612747','1610612748','1610612749','1610612750','1610612751','1610612752',
            '1610612753','1610612754','1610612755','1610612756', '1610612757','1610612758','1610612759',
            '1610612760','1610612761','1610612762','1610612763','1610612764','1610612765','1610612766']

def _team_nickname_list():
    return ['Hawks','Celtics','Cavaliers','Pelicans','Bulls',
            'Mavericks','Nuggets','Warriors','Rockets','Clippers', 'Lakers','Heat','Bucks','Timberwolves','Nets','Knicks', 'Magic','Pacers','76ers','Suns','Trail Blazers','Kings',
            'Spurs','Thunder','Raptors','Jazz','Grizzlies','Wizards',
            'Pistons','Hornets']
