import nba_api.stats.endpoints as endpoints
import requests

# Debugging Travis CI Issues
def test_dummy_test():
    assert True

def test_dummy_test2():
    assert False

def test_request_test():
    requests.get('http://google.com')

def test_nba_test():
    requests.get('http://stats.nba.com/')
    requests.get('http://stats.nba.com/stats')
    requests.get('http://stats.nba.com/stats/draftcombinestats')


def test_valid_json_boxscores():
    assert endpoints.BoxScoreAdvancedV2(game_id='0021700807').nba_response.valid_json()
    assert endpoints.BoxScoreFourFactorsV2(game_id='0021700807').nba_response.valid_json()
    assert endpoints.BoxScoreMiscV2(game_id='0021700807').nba_response.valid_json()
    assert endpoints.BoxScorePlayerTrackV2(game_id='0021700807').nba_response.valid_json()
    assert endpoints.BoxScoreScoringV2(game_id='0021700807').nba_response.valid_json()
    assert endpoints.BoxScoreSummaryV2(game_id='0021700807').nba_response.valid_json()
    assert endpoints.BoxScoreTraditionalV2(game_id='0021700807').nba_response.valid_json()
    assert endpoints.BoxScoreUsageV2(game_id='0021700807').nba_response.valid_json()

def test_valid_json_common():
    assert endpoints.CommonAllPlayers().nba_response.valid_json()
    assert endpoints.CommonPlayerInfo(player_id='2544').nba_response.valid_json()
    assert endpoints.CommonPlayoffSeries().nba_response.valid_json()
    assert endpoints.CommonTeamRoster(team_id='1610612739').nba_response.valid_json()
    assert endpoints.CommonTeamYears().nba_response.valid_json()


def test_valid_json_draft():
    #assert endpoints.DraftCombineDrillResults().nba_response.valid_json()
    assert endpoints.DraftCombineNonStationaryShooting().nba_response.valid_json()
    assert endpoints.DraftCombinePlayerAnthro().nba_response.valid_json()
    assert endpoints.DraftCombineSpotShooting().nba_response.valid_json()
    assert endpoints.DraftCombineStats().nba_response.valid_json()
    assert endpoints.DraftHistory().nba_response.valid_json()

def test_valid_json_homepage():
    assert endpoints.HomePageLeaders().nba_response.valid_json()
    assert endpoints.HomePageV2().nba_response.valid_json()
    assert endpoints.InfographicFanDuelPlayer(game_id='0021700807').nba_response.valid_json()
    assert endpoints.LeadersTiles().nba_response.valid_json()
    assert endpoints.PlayoffPicture().nba_response.valid_json()

def test_valid_json_league():
    assert endpoints.LeagueDashLineups().nba_response.valid_json()
    assert endpoints.LeagueDashPlayerBioStats().nba_response.valid_json()
    assert endpoints.LeagueDashPlayerClutch().nba_response.valid_json()
    assert endpoints.LeagueDashPlayerPtShot().nba_response.valid_json()
    assert endpoints.LeagueDashPlayerShotLocations().nba_response.valid_json()
    assert endpoints.LeagueDashPlayerStats().nba_response.valid_json()
    assert endpoints.LeagueDashPtDefend().nba_response.valid_json()
    assert endpoints.LeagueDashPtStats().nba_response.valid_json()
    assert endpoints.LeagueDashPtTeamDefend().nba_response.valid_json()
    assert endpoints.LeagueDashTeamClutch().nba_response.valid_json()
    assert endpoints.LeagueDashTeamPtShot().nba_response.valid_json()
    assert endpoints.LeagueDashTeamShotLocations().nba_response.valid_json()
    assert endpoints.LeagueDashTeamStats().nba_response.valid_json()
    assert endpoints.LeagueGameFinder().nba_response.valid_json()
    assert endpoints.LeagueGameLog().nba_response.valid_json()
    assert endpoints.LeagueLeaders().nba_response.valid_json()
    assert endpoints.LeagueStandings().nba_response.valid_json()

def test_valid_json_pbp():
    assert endpoints.PlayByPlay(game_id='0021700807').nba_response.valid_json()
    assert endpoints.PlayByPlayV2(game_id='0021700807').nba_response.valid_json()

def test_valid_json_player():
    #assert endpoints.PlayerAwards(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerCareerStats(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerCompare(player_id_list='202681,203078,2544,201567,203954',
                                   vs_player_id_list='201566,201939,201935,201142,203076').nba_response.valid_json()
    assert endpoints.PlayerDashPtPass(player_id='2544', team_id='1610612739').nba_response.valid_json()
    assert endpoints.PlayerDashPtReb(player_id='2544', team_id='1610612739').nba_response.valid_json()
    assert endpoints.PlayerDashPtShotDefend(player_id='2544', team_id='1610612739').nba_response.valid_json()
    assert endpoints.PlayerDashPtShots(player_id='2544', team_id='1610612739').nba_response.valid_json()
    assert endpoints.PlayerDashboardByClutch(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerDashboardByGameSplits(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerDashboardByGeneralSplits(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerDashboardByLastNGames(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerDashboardByOpponent(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerDashboardByShootingSplits(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerDashboardByTeamPerformance(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerDashboardByYearOverYear(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerFantasyProfile(player_id='2544').nba_response.valid_json()
    #assert endpoints.PlayerFantasyProfileBarGraph(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerGameLog(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerGameStreakFinder().nba_response.valid_json()
    assert endpoints.PlayerNextNGames(player_id='2544').nba_response.valid_json()
    assert endpoints.PlayerProfileV2(player_id='2544').nba_response.valid_json()
    #assert endpoints.PlayerVsPlayer(player_id='2544', vs_player_id='202681').nba_response.valid_json()

def test_valid_json_score():
    assert endpoints.Scoreboard().nba_response.valid_json()
    assert endpoints.ScoreboardV2().nba_response.valid_json()
    assert endpoints.ShotChartDetail(player_id='2544', team_id='1610612739').nba_response.valid_json()
    assert endpoints.ShotChartLineupDetail().nba_response.valid_json()

def test_valid_json_team():
    assert endpoints.TeamDashLineups(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashPtPass(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashPtReb(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashPtShots(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashboardByClutch(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashboardByGameSplits(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashboardByGeneralSplits(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashboardByLastNGames(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashboardByOpponent(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashboardByShootingSplits(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashboardByTeamPerformance(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDashboardByYearOverYear(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamDetails(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamGameLog(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamGameStreakFinder().nba_response.valid_json()
    assert endpoints.TeamHistoricalLeaders(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamInfoCommon(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamPlayerDashboard(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamPlayerOnOffDetails(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamPlayerOnOffSummary(team_id='1610612739').nba_response.valid_json()
    assert endpoints.TeamVsPlayer(team_id='1610612739', vs_player_id='2544').nba_response.valid_json()
    assert endpoints.TeamYearByYearStats(team_id='1610612739').nba_response.valid_json()

def test_valid_json_video():
    assert endpoints.VideoDetails(player_id='2544', team_id='1610612739').nba_response.valid_json()
    assert endpoints.VideoEvents(game_id='0021700807').nba_response.valid_json()
    assert endpoints.VideoStatus().nba_response.valid_json()

def test_valid_json_other():
    assert endpoints.DefenseHub(season='2017-18').nba_response.valid_json()
    assert endpoints.FranchiseHistory().nba_response.valid_json()
