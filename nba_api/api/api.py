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
    def __init__(self, year=None, team=None):
        self.year = year
        self.team = team

    def get_playbyplay(self, team=None, year=None, season_segment=None):      
        #team_id = self._resolve_team_ref(team)
        #season_id = self._fmt_year_as_season_id(year)
        game_id_list = self._resolve_game_ids(team_str=team, year=year, season_segment=None)

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

    def get_game_info(self, team_str=None, year=None, season_segment=None):
        return NotImplemented

        game_info_dict = {}

        team_ids = self._resolve_team_ref(team)
        season_id = self._fmt_year_as_season_id(year)
        season_segment = self._resolve_season_seg(season_segment)

        for team in team_ids:
            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team,
                                                        season_nullable=season_code,
                                                        season_type_nullable=season_seg)
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

    def get_box_scores(self):
        return NotImplemented

    def _resolve_team_ref(self, team_str=None):
        if team_str is None:
                return(pd.DataFrame(teams.get_teams())) 
        else:
                nba_teams_df = pd.DataFrame(teams.get_teams())
                return(nba_teams_df[nba_teams_df['abbreviation'].isin(team_abb)]['team_id'])

    def _fmt_year_as_season_id(self, year):
        return '{}-{}'.format(str(year), str(year + 1)[2:])
    
    def _resolve_season_seg(self, season_segment=None):
        if season_segment is None:
            return(SeasonType.regular)
        elif season_segment == 'Pre-Season':
            return(SeasonType.preseason)
        elif season_segment == 'Regular':
            return(SeasonType.regular)
        elif season_segment == 'Playoffs':
            return(SeasonTypePlayoffs.playoffs)

    def _resolve_game_ids(self, team_str=None, year=None, season_segment=None):
        team_ids = self._resolve_team_ref(team_str=team_str)
        season = self._fmt_year_as_season_id(year=year)
        season_type = self._resolve_season_seg(season_segment=season_segment)
        
        game_id_dict = {}
        
        for team in team_ids:
            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team,
                                                        season_nullable=season,
                                                        season_type_nullable=season_type)
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
