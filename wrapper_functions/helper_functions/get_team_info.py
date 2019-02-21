def get_team_info(team_abb=None):
        from nba_api.stats.static import teams
        import pandas as pd
        
        if team_abb is None:
               return(pd.DataFrame(teams.get_teams())) 
        else:
                nba_teams_df = pd.DataFrame(teams.get_teams())
                return(nba_teams_df[nba_teams_df['abbreviation'].isin(team_abb)]['id'])
        