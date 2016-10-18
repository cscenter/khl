# encoding: utf-8

import csv

from collections import defaultdict

khl_filename      = 'khl_items.csv'
idToTeam_filename = 'khl_teams.csv'
vectors           = 'vectors.csv'

# список атрибутов в khl_filename
id                                      = 'id'
timestamp                               = 'timestamp'
team1Name                               = 'team1Name'
team2Name                               = 'team2Name'
score                                   = 'score'
referees                                = 'referees'
linesmen                                = 'linesmen'
coachTeam1                              = 'coachTeam1'
coachTeam2                              = 'coachTeam2'
shotsPeriod1Team1                       = 'shotsPeriod1Team1'
shotsPeriod1Team2                       = 'shotsPeriod1Team2'
shotsPeriod2Team1                       = 'shotsPeriod2Team1'
shotsPeriod2Team2                       = 'shotsPeriod2Team2'
shotsPeriod3Team1                       = 'shotsPeriod3Team1'
shotsPeriod3Team2                       = 'shotsPeriod3Team2'
shotsOnGoalPeriod1Team1                 = 'shotsOnGoalPeriod1Team1'
shotsOnGoalPeriod1Team2                 = 'shotsOnGoalPeriod1Team2'
shotsOnGoalPeriod2Team1                 = 'shotsOnGoalPeriod2Team1'
shotsOnGoalPeriod2Team2                 = 'shotsOnGoalPeriod2Team2'
shotsOnGoalPeriod3Team1                 = 'shotsOnGoalPeriod3Team1'
shotsOnGoalPeriod3Team2                 = 'shotsOnGoalPeriod3Team2'
shotsOnGoalOvertimeTeam1                = 'shotsOnGoalOvertimeTeam1'
shotsOnGoalOvertimeTeam2                = 'shotsOnGoalOvertimeTeam2'
blockedShotsPeriod1Team1                = 'blockedShotsPeriod1Team1'
blockedShotsPeriod1Team2                = 'blockedShotsPeriod1Team2'
blockedShotsPeriod2Team1                = 'blockedShotsPeriod2Team1'
blockedShotsPeriod2Team2                = 'blockedShotsPeriod2Team2'
blockedShotsPeriod3Team1                = 'blockedShotsPeriod3Team1'
blockedShotsPeriod3Team2                = 'blockedShotsPeriod3Team2'
hitsPeriod1Team1                        = 'hitsPeriod1Team1'
hitsPeriod1Team2                        = 'hitsPeriod1Team2'
hitsPeriod2Team1                        = 'hitsPeriod2Team1'
hitsPeriod2Team2                        = 'hitsPeriod2Team2'
hitsPeriod3Team1                        = 'hitsPeriod3Team1'
hitsPeriod3Team2                        = 'hitsPeriod3Team2'
faceoffsWonPeriod1Team1                 = 'faceoffsWonPeriod1Team1'
faceoffsWonPeriod1Team2                 = 'faceoffsWonPeriod1Team2'
faceoffsWonPeriod2Team1                 = 'faceoffsWonPeriod2Team1'
faceoffsWonPeriod2Team2                 = 'faceoffsWonPeriod2Team2'
faceoffsWonPeriod3Team1                 = 'faceoffsWonPeriod3Team1'
faceoffsWonPeriod3Team2                 = 'faceoffsWonPeriod3Team2'
powerplayTimesTeam1                     = 'powerplayTimesTeam1'
powerplayTimesTeam2                     = 'powerplayTimesTeam2'
powerplayScoredTimesTeam1               = 'powerplayScoredTimesTeam1'
powerplayScoredTimesTeam2               = 'powerplayScoredTimesTeam2'
penaltykillTimesTeam1                   = 'penaltykillTimesTeam1'
penaltykillTimesTeam2                   = 'penaltykillTimesTeam2'
penaltykillAgainstTimesTeam1            = 'penaltykillAgainstTimesTeam1 '
penaltykillAgainstTimesTeam2            = 'penaltykillAgainstTimesTeam2 '
scored5vs5Team1                         = 'scored5vs5Team1'
scored5vs5Team2                         = 'scored5vs5Team2'
against5vs5Team1                        = 'against5vs5Team1'
against5vs5Team2                        = 'against5vs5Team2'
url = 'url'

# порядковые номера атрибутов в khl_filename
idToAttr = {}
idToAttr[id]                            = 0
idToAttr[timestamp]                     = 1
idToAttr[team1Name]                     = 2
idToAttr[team2Name]                     = 3
idToAttr[score]                         = 4
idToAttr[referees]                      = 5
idToAttr[linesmen]                      = 6
idToAttr[coachTeam1]                    = 7
idToAttr[coachTeam2]                    = 8
idToAttr[shotsPeriod1Team1]             = 9
idToAttr[shotsPeriod1Team2]             = 10
idToAttr[shotsPeriod2Team1]             = 11
idToAttr[shotsPeriod2Team2]             = 12
idToAttr[shotsPeriod3Team1]             = 13
idToAttr[shotsPeriod3Team2]             = 14
idToAttr[shotsOnGoalPeriod1Team1]       = 15
idToAttr[shotsOnGoalPeriod1Team2]       = 16
idToAttr[shotsOnGoalPeriod2Team1]       = 17
idToAttr[shotsOnGoalPeriod2Team2]       = 18
idToAttr[shotsOnGoalPeriod3Team1]       = 19
idToAttr[shotsOnGoalPeriod3Team2]       = 20
idToAttr[shotsOnGoalOvertimeTeam1]      = 21
idToAttr[shotsOnGoalOvertimeTeam2]      = 22
idToAttr[blockedShotsPeriod1Team1]      = 23
idToAttr[blockedShotsPeriod1Team2]      = 24
idToAttr[blockedShotsPeriod2Team1]      = 25
idToAttr[blockedShotsPeriod2Team2]      = 26
idToAttr[blockedShotsPeriod3Team1]      = 27
idToAttr[blockedShotsPeriod3Team2]      = 28
idToAttr[hitsPeriod1Team1]              = 29
idToAttr[hitsPeriod1Team2]              = 30
idToAttr[hitsPeriod2Team1]              = 31
idToAttr[hitsPeriod2Team2]              = 32
idToAttr[hitsPeriod3Team1]              = 33
idToAttr[hitsPeriod3Team2]              = 34
idToAttr[faceoffsWonPeriod1Team1]       = 35
idToAttr[faceoffsWonPeriod1Team2]       = 36
idToAttr[faceoffsWonPeriod2Team1]       = 37
idToAttr[faceoffsWonPeriod2Team2]       = 38
idToAttr[faceoffsWonPeriod3Team1]       = 39
idToAttr[faceoffsWonPeriod3Team2]       = 40
idToAttr[powerplayTimesTeam1]           = 41
idToAttr[powerplayTimesTeam2]           = 42
idToAttr[powerplayScoredTimesTeam1]     = 43
idToAttr[powerplayScoredTimesTeam2]     = 44
idToAttr[penaltykillTimesTeam1]         = 45
idToAttr[penaltykillTimesTeam2]         = 46
idToAttr[penaltykillAgainstTimesTeam1]  = 47
idToAttr[penaltykillAgainstTimesTeam2]  = 48
idToAttr[scored5vs5Team1]               = 49
idToAttr[scored5vs5Team2]               = 50
idToAttr[against5vs5Team1]              = 51
idToAttr[against5vs5Team2]              = 52
idToAttr[url]                           = 53

def loadTeamToIdDict():
    teamToId = {}
    with open(idToTeam_filename, newline='\n', encoding='utf-8') as csvfile:
        teamsreader =  csv.reader(csvfile, delimiter = ',', quotechar = '"')
        for row in teamsreader: # id, teamName
            teamToId[row[1]] = row[0]
    return teamToId

teamToId = loadTeamToIdDict()

team_statistics = [] # аккумулируемая статистика по командам (т.е. показатели после каждого матча складываются)

for i in range(0, len(teamToId)):
    team_statistics.append(defaultdict(float))

def get(event, attr):
    return event[idToAttr[attr]]

def getNum(event, attr):
    return float(get(event, attr))

# атрибуты для team_statistics
event_num                          = 'event_num'                    # номер игры для конкретной команды
team_score                         = 'team_score'                   # набранных очков в чемпионате
first_period_scored                = 'first_period_scored'
second_period_scored               = 'second_period_scored'
third_period_scored                = 'third_period_scored'
overtime_scored                    = 'overtime_scored'
first_period_against               = 'first_period_against'
second_period_against              = 'second_period_against'
third_period_against               = 'third_period_against'
overtime_against                   = 'overtime_against'
shotsOnGoalAgainst                 = 'shotsOnGoalAgainst'           # сколько нанесли ударов в стров ворот данной команде
winning_strike                     = 'winning_strike'               # число побед подряд
shotsPeriod1                       = 'shotsPeriod1Team'
shotsPeriod2                       = 'shotsPeriod2Team'
shotsPeriod3                       = 'shotsPeriod3Team'
shotsOnGoalPeriod1                 = 'shotsOnGoalPeriod1Team'
shotsOnGoalPeriod2                 = 'shotsOnGoalPeriod2Team'
shotsOnGoalPeriod3                 = 'shotsOnGoalPeriod3Team'
shotsOnGoalOvertime                = 'shotsOnGoalOvertime'
blockedShotsPeriod1                = 'blockedShotsPeriod1Team'
blockedShotsPeriod2                = 'blockedShotsPeriod2Team'
blockedShotsPeriod3                = 'blockedShotsPeriod3Team'
hitsPeriod1                        = 'hitsPeriod1Team'
hitsPeriod2                        = 'hitsPeriod2Team'
hitsPeriod3                        = 'hitsPeriod3Team'
faceoffsWonPeriod1                 = 'faceoffsWonPeriod1Team'
faceoffsWonPeriod2                 = 'faceoffsWonPeriod2Team'
faceoffsWonPeriod3                 = 'faceoffsWonPeriod3Team'
powerplayTimes                     = 'powerplayTimesTeam'
powerplayScoredTimes               = 'powerplayScoredTimesTeam'
penaltykillTimes                   = 'penaltykillTimesTeam'
penaltykillAgainstTimes            = 'penaltykillAgainstTimesTeam'
scored5vs5                         = 'scored5vs5Team'
against5vs5                        = 'against5vs5Team'

# метки для вектора
WIN_HOME = 'WinHome'
WIN_AWAY = 'WinAway'

def processEvent(event):
    # в idToTeam_filename команды пронумерованы с 1
    team1Id = int(teamToId[get(event, team1Name)]) - 1
    team2Id = int(teamToId[get(event, team2Name)]) - 1

    print("Process event: id = ", get(event, id))
    _scored = get(event, score)
    scored = _scored.split(u'\xa0')
    overtime_was = False
    team1P1Scored = int(scored[0].split(':')[0])
    team2P1Scored = int(scored[0].split(':')[1])
    team1P2Scored = int(scored[1].split(':')[0])
    team2P2Scored = int(scored[1].split(':')[1])
    team1P3Scored = int(scored[2].split(':')[0])
    team2P3Scored = int(scored[2].split(':')[1])
    team1OvScored = 0
    team2OvScored = 0
    if (len(scored) > 3):
        team1OvScored = int(scored[3].split(':')[0])
        team2OvScored = int(scored[3].split(':')[1])
        overtime_was = True
    team1Bullits = 0
    team2Bullits = 0
    if (len(scored) > 4):
        team1Bullits = int(scored[4].split(':')[0])
        team2Bullits = int(scored[4].split(':')[1])
        overtime_was = True
    team1WonGame = team1P1Scored + team1P2Scored + team1P3Scored + team1OvScored + team1Bullits > team2P1Scored \
                   + team2P2Scored + team2P3Scored + team2OvScored + team2Bullits

    min_games_threshold = 3 # или 5, но др варианты плохие однозначно
    # при векторизации не учитываются игры, в которых каждая команда сыграла не менее 3х раз
    # статистические показателя суммируются для данной игры после создания вектора
    if team_statistics[team1Id][event_num] >= min_games_threshold and team_statistics[team2Id][event_num] >= min_games_threshold:
        y = []
        if team1WonGame:
            y.append(WIN_HOME)
        else:
            y.append(WIN_AWAY)

        vector = []

        # Шайб заброшенно
        scoredTeam1 = team_statistics[team1Id][first_period_scored] + team_statistics[team1Id][second_period_scored] \
                      + team_statistics[team1Id][third_period_scored] + team_statistics[team1Id][overtime_scored]
        scoredTeam2 = team_statistics[team2Id][first_period_scored] + team_statistics[team2Id][second_period_scored] \
                      + team_statistics[team2Id][third_period_scored] + team_statistics[team2Id][overtime_scored]
        vector.append(scoredTeam1 - scoredTeam2)

        # Шайб пропущено
        againstTeam1 = team_statistics[team1Id][first_period_against] + team_statistics[team1Id][second_period_against] \
                       + team_statistics[team1Id][third_period_against] + team_statistics[team1Id][overtime_against]
        againstTeam2 = team_statistics[team2Id][first_period_against] + team_statistics[team2Id][second_period_against] \
                       + team_statistics[team2Id][third_period_against] + team_statistics[team2Id][overtime_against]
        vector.append(againstTeam1 - againstTeam2)

        # Разница заброшенных и пропущенных
        vector.append((scoredTeam1 - againstTeam1) - (scoredTeam2 - againstTeam2))

        # процент успешных игр в большинстве
        powerplayPercentageTeam1 = team_statistics[team1Id][powerplayScoredTimes] / team_statistics[team1Id][powerplayTimes]

        # процент успешности при игре в меньшинстве
        penaltyKillSuccessRateTeam1 = 1 - team_statistics[team1Id][penaltykillAgainstTimes] / team_statistics[team1Id][penaltykillTimes]
        penaltyKillSuccessRateTeam2 = 1 - team_statistics[team2Id][penaltykillAgainstTimes] / team_statistics[team2Id][penaltykillTimes]
        vector.append(penaltyKillSuccessRateTeam1 - penaltyKillSuccessRateTeam2)

        # процент реализованных броскво в створ
        # !!! добавить броски в овертайме
        shotOnTargetTeam1 = team_statistics[team1Id][shotsOnGoalPeriod1] + team_statistics[team1Id][shotsOnGoalPeriod2] \
                            + team_statistics[team1Id][shotsOnGoalPeriod3] + team_statistics[team1Id][shotsOnGoalOvertime]
        shotOnTargetTeam2 = team_statistics[team2Id][shotsOnGoalPeriod1] + team_statistics[team2Id][shotsOnGoalPeriod2] \
                            + team_statistics[team2Id][shotsOnGoalPeriod3] + team_statistics[team2Id][shotsOnGoalOvertime]
        shotPercentageTeam1 = scoredTeam1 / shotOnTargetTeam1
        shotPercentageTeam2 = scoredTeam2 / shotOnTargetTeam2
        vector.append(shotPercentageTeam1 - shotPercentageTeam2)
        print(shotPercentageTeam1 * 100, shotPercentageTeam2 * 100)

        # процент отбитых бросков в створ вратеря
        savePercentageTeam1 = 1 - againstTeam1 / team_statistics[team1Id][shotsOnGoalAgainst]
        savePercentageTeam2 = 1 - againstTeam2 / team_statistics[team2Id][shotsOnGoalAgainst]
        vector.append(savePercentageTeam1 - savePercentageTeam2)
        print(againstTeam1, team_statistics[team1Id][shotsOnGoalAgainst], againstTeam2, team_statistics[team2Id][shotsOnGoalAgainst])
        print(savePercentageTeam1 * 100, savePercentageTeam2 * 100)

        # Число побед подряд
        vector.append(team_statistics[team1Id][winning_strike] - team_statistics[team2Id][winning_strike])

        # Разница набранных очков в чемпионате
        vector.append(team_statistics[team1Id][team_score] - team_statistics[team2Id][team_score])

        ration5vs5Team1 = team_statistics[team1Id][scored5vs5] / team_statistics[team1Id][against5vs5]
        ration5vs5Team2 = team_statistics[team2Id][scored5vs5] / team_statistics[team2Id][against5vs5]
        vector.append(ration5vs5Team1 - ration5vs5Team2)

        vector.append(savePercentageTeam1 + shotPercentageTeam1 - shotPercentageTeam2 - savePercentageTeam2) # PDO

        shotsTeam1 = team_statistics[team1Id][shotsPeriod1] + team_statistics[team1Id][shotsPeriod2] + team_statistics[team1Id][shotsPeriod3]
        shotsTeam2 = team_statistics[team2Id][shotsPeriod1] + team_statistics[team2Id][shotsPeriod2] + team_statistics[team2Id][shotsPeriod3]
        vector.append(shotsTeam1 - shotsTeam2) # Fenwick

        #shotsOnGoalTeam1 = team_statistics[team1Id][shotsOnGoalPeriod1] + team_statistics[team1Id][shotsOnGoalPeriod2] + team_statistics[team1Id][shotsOnGoalPeriod3]
        #shotsOnGoalTeam2 = team_statistics[team2Id][shotsOnGoalPeriod1] + team_statistics[team2Id][shotsOnGoalPeriod2] + team_statistics[team2Id][shotsOnGoalPeriod3]
        #vector.append(shotsOnGoalTeam1 - shotsOnGoalTeam2)

        #blockedShotsTeam1 = team_statistics[team1Id][blockedShotsPeriod1] + team_statistics[team1Id][blockedShotsPeriod2] + team_statistics[team1Id][blockedShotsPeriod3]
        #blockedShotsTeam2 = team_statistics[team2Id][blockedShotsPeriod1] + team_statistics[team2Id][blockedShotsPeriod2] + team_statistics[team2Id][blockedShotsPeriod3]
        #vector.append(blockedShotsTeam2 - blockedShotsTeam1)

        #hitsTeam1 = team_statistics[team1Id][hitsPeriod1] + team_statistics[team1Id][hitsPeriod2] + team_statistics[team1Id][hitsPeriod3]
        #hitsTeam2 = team_statistics[team2Id][hitsPeriod1] + team_statistics[team2Id][hitsPeriod2] + team_statistics[team2Id][hitsPeriod3]
        #vector.append(hitsTeam1 - hitsTeam2)

        # под сомнением т.к. может быть большая разница очень
        #faceoffsWonTeam1 = team_statistics[team1Id][faceoffsWonPeriod1] + team_statistics[team1Id][faceoffsWonPeriod2] + team_statistics[team1Id][faceoffsWonPeriod3]
        #faceoffsWonTeam2 = team_statistics[team2Id][faceoffsWonPeriod1] + team_statistics[team2Id][faceoffsWonPeriod2] + team_statistics[team2Id][faceoffsWonPeriod3]
        #vector.append(faceoffsWonTeam1 - faceoffsWonTeam2)

        z = vector + y
        with open(vectors, 'a') as csvfile:
            vectrowriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            vectrowriter.writerow(z)
        # С И БЕЗ ADVANCED попробовать

    team_statistics[team1Id][event_num] += 1
    team_statistics[team2Id][event_num] += 1

    if team1WonGame:
        team_statistics[team1Id][winning_strike] += 1
        team_statistics[team2Id][winning_strike] = 0
        if overtime_was:
            team_statistics[team1Id][team_score] += 2
            team_statistics[team2Id][team_score] += 1
        else:
            team_statistics[team1Id][team_score] += 3
    else:
         team_statistics[team2Id][winning_strike] += 1
         team_statistics[team1Id][winning_strike] = 0
         if overtime_was:
            team_statistics[team2Id][team_score] += 2
            team_statistics[team1Id][team_score] += 1
         else:
            team_statistics[team2Id][team_score] += 3

    # ОТДЫХ добавиь в отдельную версию, для этого можно хранить last timestamp в teamstatistics
    # добавляй сразу в ту, что с advanced

    # scored / against
    # 1p
    team_statistics[team1Id][first_period_scored]   += team1P1Scored
    team_statistics[team2Id][first_period_scored]   += team2P1Scored
    team_statistics[team1Id][first_period_against]  += team2P1Scored
    team_statistics[team2Id][first_period_against]  += team1P1Scored
    # 2p
    team_statistics[team1Id][second_period_scored]  += team1P2Scored
    team_statistics[team2Id][second_period_scored]  += team2P2Scored
    team_statistics[team1Id][second_period_against] += team2P2Scored
    team_statistics[team2Id][second_period_against] += team1P2Scored
    # 3p
    team_statistics[team1Id][third_period_scored]   += team1P3Scored
    team_statistics[team2Id][third_period_scored]   += team2P3Scored
    team_statistics[team1Id][third_period_against]  += team2P3Scored
    team_statistics[team2Id][third_period_against]  += team1P3Scored
    # overtime
    team_statistics[team1Id][overtime_scored]       += team1OvScored
    team_statistics[team2Id][overtime_scored]       += team2OvScored
    team_statistics[team1Id][overtime_against]      += team2OvScored
    team_statistics[team2Id][overtime_against]      += team1OvScored

    team_statistics[team1Id][shotsPeriod1] += getNum(event, shotsPeriod1Team1)
    team_statistics[team2Id][shotsPeriod1] += getNum(event, shotsPeriod1Team2)
    team_statistics[team1Id][shotsPeriod2] += getNum(event, shotsPeriod2Team1)
    team_statistics[team2Id][shotsPeriod2] += getNum(event, shotsPeriod2Team2)
    team_statistics[team1Id][shotsPeriod3] += getNum(event, shotsPeriod3Team1)
    team_statistics[team2Id][shotsPeriod3] += getNum(event, shotsPeriod3Team2)

    team_statistics[team1Id][shotsOnGoalPeriod1] += getNum(event, shotsOnGoalPeriod1Team1)
    team_statistics[team2Id][shotsOnGoalPeriod1] += getNum(event, shotsOnGoalPeriod1Team2)
    team_statistics[team1Id][shotsOnGoalPeriod2] += getNum(event, shotsOnGoalPeriod2Team1)
    team_statistics[team2Id][shotsOnGoalPeriod2] += getNum(event, shotsOnGoalPeriod2Team2)
    team_statistics[team1Id][shotsOnGoalPeriod3] += getNum(event, shotsOnGoalPeriod3Team1)
    team_statistics[team2Id][shotsOnGoalPeriod3] += getNum(event, shotsOnGoalPeriod3Team2)
    team_statistics[team1Id][shotsOnGoalOvertime] += getNum(event, shotsOnGoalOvertimeTeam1)
    team_statistics[team1Id][shotsOnGoalOvertime] += getNum(event, shotsOnGoalOvertimeTeam2)
    team_statistics[team1Id][shotsOnGoalAgainst] += getNum(event, shotsPeriod1Team2) + getNum(event, shotsPeriod2Team2) \
                                                    + getNum(event, shotsPeriod3Team2) + getNum(event, shotsOnGoalOvertimeTeam2)
    team_statistics[team2Id][shotsOnGoalAgainst] += getNum(event, shotsPeriod1Team1) + getNum(event, shotsPeriod2Team1) \
                                                    + getNum(event, shotsPeriod3Team1) + getNum(event, shotsOnGoalOvertimeTeam1)

    team_statistics[team1Id][blockedShotsPeriod1] += getNum(event, blockedShotsPeriod1Team1)
    team_statistics[team2Id][blockedShotsPeriod1] += getNum(event, blockedShotsPeriod1Team2)
    team_statistics[team1Id][blockedShotsPeriod2] += getNum(event, blockedShotsPeriod2Team1)
    team_statistics[team2Id][blockedShotsPeriod2] += getNum(event, blockedShotsPeriod2Team2)
    team_statistics[team1Id][blockedShotsPeriod3] += getNum(event, blockedShotsPeriod3Team1)
    team_statistics[team2Id][blockedShotsPeriod3] += getNum(event, blockedShotsPeriod3Team2)

    team_statistics[team1Id][hitsPeriod1] += getNum(event, hitsPeriod1Team1)
    team_statistics[team2Id][hitsPeriod1] += getNum(event, hitsPeriod1Team2)
    team_statistics[team1Id][hitsPeriod2] += getNum(event, hitsPeriod2Team1)
    team_statistics[team2Id][hitsPeriod2] += getNum(event, hitsPeriod2Team2)
    team_statistics[team1Id][hitsPeriod3] += getNum(event, hitsPeriod3Team1)
    team_statistics[team2Id][hitsPeriod3] += getNum(event, hitsPeriod3Team2)

    team_statistics[team1Id][faceoffsWonPeriod1] += getNum(event, faceoffsWonPeriod1Team1)
    team_statistics[team2Id][faceoffsWonPeriod1] += getNum(event, faceoffsWonPeriod1Team2)
    team_statistics[team1Id][faceoffsWonPeriod2] += getNum(event, faceoffsWonPeriod2Team1)
    team_statistics[team2Id][faceoffsWonPeriod2] += getNum(event, faceoffsWonPeriod2Team2)
    team_statistics[team1Id][faceoffsWonPeriod3] += getNum(event, faceoffsWonPeriod3Team1)
    team_statistics[team2Id][faceoffsWonPeriod3] += getNum(event, faceoffsWonPeriod3Team2)

    team_statistics[team1Id][powerplayTimes] += getNum(event, powerplayTimesTeam1)
    team_statistics[team2Id][powerplayTimes] += getNum(event, powerplayTimesTeam2)
    team_statistics[team1Id][powerplayScoredTimes] += getNum(event, powerplayScoredTimesTeam1)
    team_statistics[team2Id][powerplayScoredTimes] += getNum(event, powerplayScoredTimesTeam2)

    team_statistics[team1Id][penaltykillTimes] += getNum(event, penaltykillTimesTeam1)
    team_statistics[team2Id][penaltykillTimes] += getNum(event, penaltykillTimesTeam2)
    team_statistics[team1Id][penaltykillAgainstTimes] += getNum(event, penaltykillAgainstTimesTeam1)
    team_statistics[team2Id][penaltykillAgainstTimes] += getNum(event, penaltykillAgainstTimesTeam2)

    team_statistics[team1Id][scored5vs5] += getNum(event, scored5vs5Team1)
    team_statistics[team2Id][scored5vs5] += getNum(event, scored5vs5Team2)
    team_statistics[team1Id][against5vs5] += getNum(event, against5vs5Team1)
    team_statistics[team2Id][against5vs5] += getNum(event, against5vs5Team2)

def main():
    events = []
    with open(khl_filename, newline='\n', encoding='utf-8') as csvfile:
        eventreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
        for event in eventreader:
            if event[idToAttr[id]] == 'id':
                continue
            events.append(event)

    events.sort(key = lambda x : int(x[0]))
    for event in events:
        processEvent(event)

if __name__ == '__main__':
    main()