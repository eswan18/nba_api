### Should I try to remove summer league games? Or make a note and in the package and let people filter by date?
# the teams class provides multiple name identificiations for a team.
# by abbr, full name, city, nickname
# i'll start with abbr, but it would be a nice to have to have all

import pandas as pd
from nba_api.stats.endpoints import playbyplay
from wrapper_functions.helper_functions.get_team_info import get_team_info
from wrapper_functions.helper_functions.get_game_info import get_game_info
from wrapper_functions.helper_functions.get_game_ids import get_game_ids
from wrapper_functions.helper_functions.event_msg_type_desc import event_msg_type_desc
from time import sleep

def get_playbyplay(team_abb=None, season=None, season_segment=None):
        # call get_teams method and store as data frame
        # filter df based on team_abb argument and collect teamid
        nba_teams_df = get_team_info()
        team_ids = list(nba_teams_df[nba_teams_df['abbreviation'].isin(team_abb)]['id'])
        
        # collect game_ids for each team
        game_id_list = get_game_ids(team_id = team_ids, season = season, season_type = season_segment)

        # collect game info for each team
        game_info_df = get_game_info(team_id = team_ids, season = season, season_type = season_segment)

        # Start an empty dict
        pbp_data_dict = {}
        
        # Call PlayByPlay for every game_id. Store in pbp_data_dict
        for game_id in game_id_list:
                df = playbyplay.PlayByPlay(game_id).get_data_frames()[0]
                pbp_data_dict[game_id] = df
                sleep(1)

        # Get dict keys
        dict_keys = pbp_data_dict.keys()
        # Create list of pbp data frames 
        frames = [pbp_data_dict[key] for key in dict_keys]
        # Union the data frame in frames
        pbp_df = pd.concat(frames, axis=0)

        # Convert dtypes
        pbp_df['GAME_ID'] = pbp_df['GAME_ID'].astype(str)
        pbp_df['EVENTNUM'] = pbp_df['EVENTNUM'].astype(str).astype(int)
        pbp_df['EVENTMSGTYPE'] = pbp_df['EVENTMSGTYPE'].astype(str).astype(int)
        pbp_df['EVENTMSGACTIONTYPE'] = pbp_df['EVENTMSGACTIONTYPE'].astype(str).astype(int)
        pbp_df['PERIOD'] = pbp_df['PERIOD'].astype(str).astype(int)
        pbp_df['PCTIMESTRING'] = pbp_df['PCTIMESTRING'].astype(str)
        pbp_df['HOMEDESCRIPTION'] = pbp_df['HOMEDESCRIPTION'].astype(str)
        pbp_df['NEUTRALDESCRIPTION'] = pbp_df['NEUTRALDESCRIPTION'].astype(str)
        pbp_df['VISITORDESCRIPTION'] = pbp_df['VISITORDESCRIPTION'].astype(str)
        pbp_df['SCORE'] = pbp_df['SCORE'].astype(str)
        pbp_df['SCOREMARGIN'] = pbp_df['SCOREMARGIN'].astype(str) ## can't convert to int without dealing with None values

        # Add date to pbp_df
        pbp_df = pbp_df.merge(game_info_df[['GAME_ID', 'GAME_DATE']], on=['GAME_ID'], how='inner')

        # Add home/away column

        # Add column to ID which team is on offense

        # Add event message descriptions to df
        pbp_df['EVENTMSGTYPE_DESC'] = pbp_df['EVENTMSGTYPE'].apply(event_msg_type_desc)

        # Add event action description 
        #pbp_df['EVENTMSGACTION_DESC'] = pbp.df['EVENTMSGACTIONTYPE'].apply(event_mgs_action_desc)

        # Return
        return(pbp_df)
