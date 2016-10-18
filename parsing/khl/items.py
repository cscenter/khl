# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class KhlItem(Item):
    id                            = Field() # номер матча на khl.ru - там они пронумерованы по возрастанию даты
    timestamp                     = Field() # дата и время матча 01.11.2015
    team1Name                     = Field() # название первой команды
    team2Name                     = Field() # название второй команды
    score                         = Field() # результат матча в формате "1:1 1:2 1:0 0:0 1:0" или "1:0 0:2 1:3" или 1:0 0:2 2:1 1:0"
    referees                      = Field() # главные судьи
    linesmen                      = Field() # линейные судьи
    coachTeam1                    = Field() # тренер первой команды
    coachTeam2                    = Field() # тренер второй команды
    shotsPeriod1Team1             = Field() # броски, в первом периоде, всего (в створ и мимо, блокированные не считаются) первой команды
    shotsPeriod1Team2             = Field() # броски, в первом периоде, всего (в створ и мимо, блокированные не считаются) второй команды
    shotsPeriod2Team1             = Field() # броски, во втором периоде, всего (в створ и мимо, блокированные не считаются) первой команды
    shotsPeriod2Team2             = Field() # броски, во втором периоде, всего (в створ и мимо, блокированные не считаются) второй команды
    shotsPeriod3Team1             = Field() # броски, в третьем периоде, всего (в створ и мимо, блокированные не считаются) первой команды
    shotsPeriod3Team2             = Field() # броски, в третьем периоде, всего (в створ и мимо, блокированные не считаются) второй команды
    shotsOnGoalPeriod1Team1       = Field() # броски в створ, всего в первом периоде первой команды
    shotsOnGoalPeriod1Team2       = Field() # броски в створ, всего в первом периоде второй команды
    shotsOnGoalPeriod2Team1       = Field() # броски в створ, всего во втором периоде первой команды
    shotsOnGoalPeriod2Team2       = Field() # броски в створ, всего во втором периоде второй команды
    shotsOnGoalPeriod3Team1       = Field() # броски в створ, всего в третьем периоде первой команды
    shotsOnGoalPeriod3Team2       = Field() # броски в створ, всего в третьем периоде второй команды
    shotsOnGoalOvertimeTeam1      = Field() # броски в створ, всего в овертайме первой команды
    shotsOnGoalOvertimeTeam2      = Field() # броски в створ, всего в овертайме второй команды
    blockedShotsPeriod1Team1      = Field() # блокированные броски, всего в первом периоде для первой команды
    blockedShotsPeriod1Team2      = Field() # блокированные броски, всего в первом периоде для второй команды    
    blockedShotsPeriod2Team1      = Field() # блокированные броски, всего во втором периоде для первой команды
    blockedShotsPeriod2Team2      = Field() # блокированные броски, всего во втором периоде для второй команды    
    blockedShotsPeriod3Team1      = Field() # блокированные броски, всего в третьем периоде для первой команды
    blockedShotsPeriod3Team2      = Field() # блокированные броски, всего в третьем периоде для второй команды
    hitsPeriod1Team1              = Field() # силовые приемы в первом периоде для первой команды
    hitsPeriod1Team2              = Field() # силовые приемы в первом периоде для второй команды
    hitsPeriod2Team1              = Field() # силовые приемы во втором периоде для первой команды
    hitsPeriod2Team2              = Field() # силовые приемы во втором периоде для второй команды
    hitsPeriod3Team1              = Field() # силовые приемы в третьем периоде для первой команды
    hitsPeriod3Team2              = Field() # силовые приемы в третьем периоде для второй команды
    faceoffsWonPeriod1Team1       = Field() # количество выигранных в первом вериоде взбрасываний первая команда
    faceoffsWonPeriod1Team2       = Field() # количество выигранных взбрасываний вторая команда
    faceoffsWonPeriod2Team1       = Field() # количество выигранных взбрасываний первая команда
    faceoffsWonPeriod2Team2       = Field() # количество выигранных взбрасываний вторая команда
    faceoffsWonPeriod3Team1       = Field() # количество выигранных взбрасываний первая команда
    faceoffsWonPeriod3Team2       = Field() # количество выигранных взбрасываний вторая команда
    powerplayTimesTeam1           = Field() # количество раз когда первая команда играла в большинстве
    powerplayTimesTeam2           = Field() # количество раз когда вторая команда играла в большинстве
    powerplayScoredTimesTeam1     = Field() # количество реализованных попыток большинства для первой команды
    powerplayScoredTimesTeam2     = Field() # количество реализованных попыток большинства для второй команды
    penaltykillTimesTeam1         = Field() # количество раз когда первая команда играла в меньшинстве
    penaltykillTimesTeam2         = Field() # количество раз когда вторая команда играла в меньшинстве
    penaltykillAgainstTimesTeam1  = Field() # количество раз когда первая команда пропускала в меньшинстве
    penaltykillAgainstTimesTeam2  = Field() # количество раз когда вторая команда пропускала в меньшинстве
    scored5vs5Team1               = Field() # забитые шайбы первой командой в полном составе, количество
    scored5vs5Team2               = Field() # забитые шайбы второй командой в полном составе, количество
    against5vs5Team1              = Field() # пропущенные шайбы первой командой в полном составе, количество
    against5vs5Team2              = Field() # пропущенные шайбы второй командой в полном составе, количество
    url                           = Field() # url странички откуда получены данные
        