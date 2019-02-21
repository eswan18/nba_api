def get_playbyplay(team_abb, year=None, season_segment=None):
        # collect team info
        # the teams class provides multiple name identificiations for a team.
        # by abbr, full name, city, nickname
        # i'll start with abbr, but it would be a nice to have to have all
        
        # call get_teams method and store as data frame
        import pandas as pd
        from helper_functions import get_teams
        from helper_functions import get_game_ids
        from helper_functions import event_msg_desc
        
        # filter df based on team argument and collect teamid
        nba_teams_df = get_teams()
        team_ids = nba_teams_df[nba_teams_df['abbreviation'].isin(team_abb)]['id']
        
        # collect game_ids
        game_id_list = get_game_ids(team_ids)        
        
        # Retrieving play by play for each game
        pbp_data_dict = {}
        
        for game_id in game_id_list:
            df = playbyplay.PlayByPlay(game_id).get_data_frames()[0]
            
            pbp_data_dict[game_id] = df

        pbp_df = pd.from_dict(pbp_data_dict)

        pbp_df['EVENTMSGDESC'] = pbp_df.apply(event_mgs_desc, axis=1)
