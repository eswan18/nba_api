from nba_api.stats.static import teams
from nba_api.stats.endpoints import playbyplay
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType
from nba_api.stats.library.parameters import SeasonTypePlayoffs
from nba_api.stats.library.parameters import SeasonID
from time import sleep
import pandas as pd
import numpy as np

class API():
    def __init__(self, year=None, team=None, season_segment=None):
        self.year = year
        self.team = team
        self.season_segment = season_segment

    def get_playbyplay(self, team, year, season_segment):      
        game_id_list = self._resolve_game_ids(team=team, year=year, season_segment=season_segment)
        
        # collect game info for each team
        game_info_df = self.get_game_info(team=team, year=year, season_segment=season_segment)

        # Start an empty dict
        pbp_data_dict = {}
        
        # Call PlayByPlay for every game_id. Store in pbp_data_dict
        for game_id in game_id_list:
                df = playbyplay.PlayByPlay(game_id).get_data_frames()[0]
                pbp_data_dict[game_id] = df
                sleep(np.random.gamma(shape=1.75, scale=2.0, size=None))

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

        # Add event action description 
        #pbp_df['EVENTMSGACTION_DESC'] = pbp.df['EVENTMSGACTIONTYPE'].apply(event_mgs_action_desc)

        # Return
        return(pbp_df)
    
    def get_box_scores(self, team, year, season_segment):
        return NotImplemented

    def get_game_info(self, team, year, season_segment):
        game_info_dict = {}

        team_ids = self._resolve_team_ref_to_df(team)['id']
        season_id = self._fmt_year_as_season_id(year)
        season_segment = self._resolve_season_seg(season_segment)

        for team in team_ids:
            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team,
                                                        season_nullable=season_id,
                                                        season_type_nullable=season_segment)
            game_info_dict0 = gamefinder.get_normalized_dict()
            game_info_dict1 = game_info_dict0['LeagueGameFinderResults']
            game_info_df = pd.DataFrame(game_info_dict1)
            game_info_dict[team] = game_info_df
            
        # collect dictionary keys into a list
        dict_keys = game_info_dict.keys()
        # Create list of game info dataframes 
        frames = [game_info_dict[key] for key in dict_keys]
        # Union the dataframes in frames
        fin_game_info_df = pd.concat(frames, axis=0)

        # Convert dtypes
        fin_game_info_df['GAME_ID'] = fin_game_info_df['GAME_ID'].astype('str')
        fin_game_info_df['GAME_DATE'] = fin_game_info_df['GAME_DATE'].astype('datetime64[ns]')
        fin_game_info_df['MATCHUP'] = fin_game_info_df['MATCHUP'].astype('str')
        fin_game_info_df['SEASON_ID'] = fin_game_info_df['SEASON_ID'].astype('str')
        fin_game_info_df['TEAM_ABBREVIATION'] = fin_game_info_df['TEAM_ABBREVIATION'].astype('str')
        fin_game_info_df['TEAM_NAME'] = fin_game_info_df['TEAM_NAME'].astype('str')
        fin_game_info_df['WL'] = fin_game_info_df['WL'].astype('str')

        # return the finished data frame
        return(fin_game_info_df)

    def _resolve_team_ref_to_df(self, team):
        nba_teams_df = pd.DataFrame(teams.get_teams())
        
        team_abb_list = teams._team_abb_list()
        team_fn_list = teams._team_full_name_list()
        team_id_list = teams._team_id_list()
        team_nn_list = teams._team_nickname_list()
        
        if team is None:
            return(nba_teams_df)
        elif team[0] in team_abb_list:
            return(nba_teams_df[nba_teams_df['abbreviation'].isin(team)])
        elif team[0] in team_fn_list:
            return(nba_teams_df[nba_teams_df['full_name'].isin(team)])
        elif team[0] in team_id_list:
            return(nba_teams_df[nba_teams_df['id'].isin(team)])
        elif team[0] in team_nn_list:
            return(nba_teams_df[nba_teams_df['nickname'].isin(team)])
        else:
            return(nba_teams_df)
        
    def _resolve_team_id(self, team):
        team_info_df = self._resolve_team_ref_to_df(team)

        return(team_info_df['id'])

    def _fmt_year_as_season_id(self, year):
        return '{}-{}'.format(str(year), str(year + 1)[2:])
    
    def _resolve_season_seg(self, season_segment):
        if season_segment is None:
            return(SeasonType.regular)
        elif season_segment == 'Pre-Season':
            return(SeasonType.preseason)
        elif season_segment == 'Regular':
            return(SeasonType.regular)
        elif season_segment == 'Playoffs':
            return(SeasonTypePlayoffs.playoffs)

    def _resolve_game_ids(self, team, year, season_segment):
        team_ids = self._resolve_team_id(team=team)
        season = self._fmt_year_as_season_id(year=year)
        season_segment = self._resolve_season_seg(season_segment=season_segment)
        
        game_id_dict = {}
        
        for team in team_ids:
            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team,
                                                        season_nullable=season,
                                                        season_type_nullable=season_segment)
            game_info_dict0 = gamefinder.get_normalized_dict()
            game_info_dict1 = game_info_dict0['LeagueGameFinderResults']
            game_info_df = pd.DataFrame(game_info_dict1)
            game_id_list = list(game_info_df['GAME_ID'])
            game_id_dict[team] = game_id_list
            
        # extract unique dictionary values
        ll = list(game_id_dict.values())
        l = [item for sublist in ll for item in sublist]
        return(list(set(l)))
    
    
         
    def _get_event_msg_type_desc(self, event_msg_type):
        return NotImplemented
