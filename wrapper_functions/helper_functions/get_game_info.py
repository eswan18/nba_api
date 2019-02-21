from wrapper_functions.helper_functions.get_team_info import get_team_info
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType
from nba_api.stats.library.parameters import SeasonTypePlayoffs
from nba_api.stats.library.parameters import SeasonID
import pandas as pd

game_info_dict = {}

def get_game_info(team_id=None, season=None, season_type=None):
        # Define teams
        if team_id is None:
            team_info = get_team_info()
            team_ids = team_info['id']
        else:
            team_ids = team_id

        # Define season
        if season is None:
            season_code = Season.default
        else:
            season_code  = '{}-{}'.format(season, str(season + 1)[2:])

        # Define Season Type
        if season_type is None:
            season_seg = SeasonType.regular
        elif season_type == 'Pre-Season':
            season_seg = SeasonType.preseason
        elif season_type == 'Regular':
            season_seg = SeasonType.regular
        elif season_type == 'Playoffs':
            season_seg = SeasonTypePlayoffs.playoffs
            

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