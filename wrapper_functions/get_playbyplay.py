def get_playbyplay(team_abb, year=None, season_segment=None):
        # collect team info
        # the teams class provides multiple name identificiations for a team.
        # by abbr, full name, city, nickname
        # i'll start with abbr, but it would be a nice to have to have all
        
        # call get_teams method and store as data frame
        import pandas as pd
        from helper_functions import get_teams
        
        # filter df based on team argument and collect teamid
        nba_teams_df = get_teams()
        team_ids = nba_teams_df[nba_teams_df['abbreviation'].isin(team_abb)]['id']
        
        # collect game_ids 
        from nba_api.stats.endpoints import leaguegamefinder
        
        game_id_dict = {}
    
        for team in team_ids:
            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team,
                                    season_nullable=Season.default,
                                    season_type_nullable=SeasonType.regular)
            
            game_info_df = gamefinder.get_normalized_dict()
            game_id_list = pd.DataFrame(games_dict['LeagueGameFinderResults'])['GAME_ID']

            game_id_dict(team) = game_id_list
        
        # extract unique dictionary values
        l = list(game_id_dict.values())
        game_id_list = list(set([item for sublist in l for item in sublist]))        
        
        # Retrieving play by play for each game
        pbp_data_dict = {}
        
        for game_id in game_id_list:
            df = playbyplay.PlayByPlay(game_id).get_data_frames()[0]
            
            pbp_data_dict[game_id] = df