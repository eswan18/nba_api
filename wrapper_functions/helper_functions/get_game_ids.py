def get_game_ids(team_ids=None):
    import get_team_info
    from nba_api.stats.endpoints import leaguegamefinder
    from wrapper_functions.helper_functions import get_team_info

    game_id_dict = {}

    if team_ids is None:
        team_info = get_team_info()
        team_ids = team_info['id']

        for team in team_ids:
            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team,
                                    season_nullable=Season.default,
                                    season_type_nullable=SeasonType.regular)
            
            game_info_df = gamefinder.get_normalized_dict()
            game_id_list = pd.DataFrame(games_dict['LeagueGameFinderResults'])['GAME_ID']
            game_id_dict(team) = game_id_list
    
            # extract unique dictionary values
            l = list(game_id_dict.values())
            return(list(set([item for sublist in l for item in sublist]))
    
    else:
        team_info = get_team_info()
        team_ids = team_info[team_info['abbreviation'].isin(team_abb)]['id']

        for team in team_ids:
            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team,
                                    season_nullable=Season.default,
                                    season_type_nullable=SeasonType.regular)
            
            game_info_df = gamefinder.get_normalized_dict()
            game_id_list = pd.DataFrame(games_dict['LeagueGameFinderResults'])['GAME_ID']
            game_id_dict(team) = game_id_list
    
            # extract unique dictionary values
            l = list(game_id_dict.values())
            return(list(set([item for sublist in l for item in sublist]))