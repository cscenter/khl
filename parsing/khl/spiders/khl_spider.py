# -*- coding: utf-8 -*-

import re
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from khl.items import KhlItem


class KhlLoader(XPathItemLoader):
    default_input_processor = MapCompose(lambda s: re.sub('\s+', ' ', s.strip()))
    default_output_processor = TakeFirst()


class KhlSpider(CrawlSpider):
    name = "khl"
    allowed_domains = ["khl.ru"]    
    #start_urls = ["http://www.khl.ru/calendar/309/00/"] # календарь всех игр 2015-2016 сезона
    start_urls = ["http://www.khl.ru/game/309/46649/protocol/"] # календарь всех игр 2015-2016 сезона

    rules = (
             Rule(SgmlLinkExtractor(allow=('/protocol')), callback='parse_item'),
             )

    shotsPeriod1Team1 = '-1'
    shotsPeriod1Team2 = '-1'
    shotsPeriod2Team1 = '-1'
    shotsPeriod2Team2 = '-1'
    shotsPeriod3Team1 = '-1'
    shotsPeriod3Team2 = '-1'
    faceoffsWonPeriod1Team1 = '-1'
    faceoffsWonPeriod1Team2 = '-1'
    faceoffsWonPeriod2Team1 = '-1'
    faceoffsWonPeriod2Team2 = '-1'
    faceoffsWonPeriod3Team1 = '-1'
    faceoffsWonPeriod3Team2 = '-1'

    def extractFromLive(self, items, broski, faceoff, statistics_after_1_period, statistics_after_2_period, statistics_after_3_period):
        global shotsPeriod1Team1
        global shotsPeriod1Team2
        global shotsPeriod2Team1
        global shotsPeriod2Team2
        global shotsPeriod3Team1
        global shotsPeriod3Team2
        global faceoffsWonPeriod1Team1
        global faceoffsWonPeriod1Team2
        global faceoffsWonPeriod2Team1
        global faceoffsWonPeriod2Team2
        global faceoffsWonPeriod3Team1
        global faceoffsWonPeriod3Team2
        for item in items:
            pos = item.find(statistics_after_1_period)
            if pos != -1:
                only_useful = item[pos:]
                broski_index = only_useful.find(broski)
                to = only_useful.find(u';')
                shots = only_useful[(broski_index + len(broski) + 2) : (to - 1)]
                faceoffs_index = only_useful.find(faceoff)
                to2 = only_useful[faceoffs_index:].find(u';')
                faceoffs = only_useful[(faceoffs_index + len(faceoff) + 2) : (faceoffs_index + to2 - 1)]
                shotsPeriod1Team1 = shots.split("-")[0]
                shotsPeriod1Team2 = shots.split("-")[1]
                faceoffsWonPeriod1Team1 = faceoffs.split("-")[0]
                faceoffsWonPeriod1Team2 = faceoffs.split("-")[1]
            pos2 = item.find(statistics_after_2_period)
            if pos2 != -1:
                only_useful = item[pos2:]
                broski_index = only_useful.find(broski)
                to = only_useful.find(u';')
                shots = only_useful[(broski_index + len(broski) + 2) : (to - 1)]
                faceoffs_index = only_useful.find(faceoff)
                to2 = only_useful[faceoffs_index:].find(u';')
                faceoffs = only_useful[(faceoffs_index + len(faceoff) + 2) : (faceoffs_index + to2 - 1)]
                shotsPeriod2Team1 = shots.split("-")[0]
                shotsPeriod2Team2 = shots.split("-")[1]
                faceoffsWonPeriod2Team1 = faceoffs.split("-")[0]
                faceoffsWonPeriod2Team2 = faceoffs.split("-")[1]
            pos3 = item.find(statistics_after_3_period)
            if pos3 != -1:
                only_useful = item[pos3:]
                broski_index = only_useful.find(broski)
                to = only_useful.find(u';')
                shots = only_useful[(broski_index + len(broski) + 2) : (to - 1)]
                faceoffs_index = only_useful.find(faceoff)
                to2 = only_useful[faceoffs_index:].find(u';')
                faceoffs = only_useful[(faceoffs_index + len(faceoff) + 2) : (faceoffs_index + to2 - 1)]
                shotsPeriod3Team1 = shots.split("-")[0]
                shotsPeriod3Team2 = shots.split("-")[1]
                faceoffsWonPeriod3Team1 = faceoffs.split("-")[0]
                faceoffsWonPeriod3Team2 = faceoffs.split("-")[1]

    def parse_text(self, response):
        # текстовые трансляции text.khl.ru за сезон 2015-2016 двух типов. Почти все javascript
        # но последнии пару десятков (из 840) представлены в том же формате, что и /protocol/

        l = response.meta['item']
        items = response.xpath('//script/text()')[0].re(".*olEvents.*")

        global shotsPeriod1Team1
        global shotsPeriod1Team2
        global shotsPeriod2Team1
        global shotsPeriod2Team2
        global shotsPeriod3Team1
        global shotsPeriod3Team2
        global faceoffsWonPeriod1Team1
        global faceoffsWonPeriod1Team2
        global faceoffsWonPeriod2Team1
        global faceoffsWonPeriod2Team2
        global faceoffsWonPeriod3Team1
        global faceoffsWonPeriod3Team2

        shotsPeriod1Team1 = '-1'
        shotsPeriod1Team2 = '-1'
        shotsPeriod2Team1 = '-1'
        shotsPeriod2Team2 = '-1'
        shotsPeriod3Team1 = '-1'
        shotsPeriod3Team2 = '-1'
        faceoffsWonPeriod1Team1 = '-1'
        faceoffsWonPeriod1Team2 = '-1'
        faceoffsWonPeriod2Team1 = '-1'
        faceoffsWonPeriod2Team2 = '-1'
        faceoffsWonPeriod3Team1 = '-1'
        faceoffsWonPeriod3Team2 = '-1'

        # javascript
        self.extractFromLive(items, u'Броски', u'Вбрасывания', u'Статистика 1-го периода', u'Статистика 2-го периода', u'Статистика 3-го периода')
        self.extractFromLive(items, u'Shots', u'Faceoffs won', u'Stats of 1st period', u'Stats of 2nd period', u'Stats of 3rd period')
        self.extractFromLive(items, u'Shots', u'Faceoffs won', u'Stats of 1-st period', u'Stats of 2-nd period', u'Stats of 3-rd period')
        self.extractFromLive(items, u'Shots', u'Faceoffs won', u'Stats of 1-st period', u'Stats of 2-st period', u'Stats of 3-st period')
        self.extractFromLive(items, u'Shots', u'Faceoffs won', u'Stats of 1st period', u'Stats of 2st period', u'Stats of 3st period')

        # уже не javascript
        statistics_after_1_period = u'Статистика 1-го периода'
        statistics_after_2_period = u'Статистика 2-го периода'   
        statistics_after_3_period = u'Статистика 3-го периода'      
        broski = u'Броски'
        faceoff = u'Вбрасывания'
        anotherFormatList = response.xpath('//li[@class="b-text_translation_item"]//div[@class="b-right m-txt"]//p[@class="e-action_txt"]//text()').extract()  
        for i in range(len(anotherFormatList)):
            item = anotherFormatList[i]
            if item == (statistics_after_1_period + ':'):
                stats_item = anotherFormatList[i + 1]
                broski_index = stats_item.find(u";")
                shots = stats_item[(len(broski) + 4) : (broski_index - 1)]
                shotsPeriod1Team1 = shots.split('-')[0]
                shotsPeriod1Team2 = shots.split('-')[1]
                faceoffs_index = stats_item.find(faceoff)
                to2 = stats_item[faceoffs_index:].find(u';')
                faceoffs = stats_item[(faceoffs_index + len(faceoff) + 2) : (faceoffs_index + to2 - 1)]
                faceoffsWonPeriod1Team1 = faceoffs.split("-")[0]
                faceoffsWonPeriod1Team2 = faceoffs.split("-")[1]  
            if item == (statistics_after_2_period + ':'):
                stats_item = anotherFormatList[i + 1]
                broski_index = stats_item.find(u";")
                shots = stats_item[(len(broski) + 4) : (broski_index - 1)]
                shotsPeriod2Team1 = shots.split('-')[0]
                shotsPeriod2Team2 = shots.split('-')[1]
                faceoffs_index = stats_item.find(faceoff)
                to2 = stats_item[faceoffs_index:].find(u';')
                faceoffs = stats_item[(faceoffs_index + len(faceoff) + 2) : (faceoffs_index + to2 - 1)]
                faceoffsWonPeriod2Team1 = faceoffs.split("-")[0]
                faceoffsWonPeriod2Team2 = faceoffs.split("-")[1]              
            if item == (statistics_after_3_period + ':'):
                stats_item = anotherFormatList[i + 1]
                broski_index = stats_item.find(u";")
                shots = stats_item[(len(broski) + 4) : (broski_index - 1)]
                shotsPeriod3Team1 = shots.split('-')[0]
                shotsPeriod3Team2 = shots.split('-')[1]
                faceoffs_index = stats_item.find(faceoff)
                to2 = stats_item[faceoffs_index:].find(u';')
                faceoffs = stats_item[(faceoffs_index + len(faceoff) + 2) : (faceoffs_index + to2 - 1)]
                faceoffsWonPeriod3Team1 = faceoffs.split("-")[0]
                faceoffsWonPeriod3Team2 = faceoffs.split("-")[1]  
        
        l.add_xpath('shotsPeriod1Team1', str(shotsPeriod1Team1))
        l.add_xpath('shotsPeriod1Team2', shotsPeriod1Team2)
        l.add_xpath('shotsPeriod2Team1', shotsPeriod2Team1)
        l.add_xpath('shotsPeriod2Team2', shotsPeriod2Team2)
        l.add_xpath('shotsPeriod3Team1', shotsPeriod3Team1)
        l.add_xpath('shotsPeriod3Team2', shotsPeriod3Team2)
        
        l.add_xpath('faceoffsWonPeriod1Team1', faceoffsWonPeriod1Team1)
        l.add_xpath('faceoffsWonPeriod1Team2', faceoffsWonPeriod1Team2)
        l.add_xpath('faceoffsWonPeriod2Team1', faceoffsWonPeriod2Team1)
        l.add_xpath('faceoffsWonPeriod2Team2', faceoffsWonPeriod2Team2)
        l.add_xpath('faceoffsWonPeriod3Team1', faceoffsWonPeriod3Team1)
        l.add_xpath('faceoffsWonPeriod3Team2', faceoffsWonPeriod3Team2)  
        
        return l.load_item()

    def parse_item(self, response):
        splited = response.url.split('game/')        
        if splited[1].startswith("309") == False: # если не весть каким образом оказались не в сезоне 2015-2016
            return        
            
        hxs = HtmlXPathSelector(response)

        item = KhlItem()
        l = KhlLoader(item, hxs)
        
        l.add_xpath('id', '//span[re:test(@class, "e-num")]/text()')
        l.add_xpath('timestamp', '//li[re:test(@class, "b-match_add_info_item")]/span/text()', lambda x: x[1])
        l.add_xpath('team1Name', '//h3[re:test(@class, "e-club_name")]/text()', lambda x: x[0])
        l.add_xpath('team2Name', '//h3[re:test(@class, "e-club_name")]/text()', lambda x: x[1])
        l.add_xpath('score', '//dd[re:test(@class, "b-period_score")]/text()')
        l.add_xpath('referees', '//li[re:test(@class, "b-match_add_info_item")]/span/text()', lambda x: x[7])
        l.add_xpath('linesmen', '//li[re:test(@class, "b-match_add_info_item")]/span/text()', lambda x: x[8])
        l.add_xpath('coachTeam1', '//ul[re:test(@class, "e-player_honors")]/text()', lambda x: x[0])
        l.add_xpath('coachTeam2', '//ul[re:test(@class, "e-player_honors")]/text()', lambda x: x[1])

        # индексы в таблице
        shotsOnGoalPeriod1Team1 = 6
        shotsOnGoalPeriod1Team2 = 12
        shotsOnGoalPeriod2Team1 = 22
        shotsOnGoalPeriod2Team2 = 28
        shotsOnGoalPeriod3Team1 = 38
        shotsOnGoalPeriod3Team2 = 44
        l.add_xpath('shotsOnGoalPeriod1Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[shotsOnGoalPeriod1Team1])
        l.add_xpath('shotsOnGoalPeriod1Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[shotsOnGoalPeriod1Team2])
        l.add_xpath('shotsOnGoalPeriod2Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[shotsOnGoalPeriod2Team1])
        l.add_xpath('shotsOnGoalPeriod2Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[shotsOnGoalPeriod2Team2])
        l.add_xpath('shotsOnGoalPeriod3Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[shotsOnGoalPeriod3Team1])
        l.add_xpath('shotsOnGoalPeriod3Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[shotsOnGoalPeriod3Team2])

        # индексы в таблице
        blockedShotsPeriod1Team1 = 81
        blockedShotsPeriod1Team2 = 85
        blockedShotsPeriod2Team1 = 93
        blockedShotsPeriod2Team2 = 97
        blockedShotsPeriod3Team1 = 105
        blockedShotsPeriod3Team2 = 109
        hitsPeriod1Team1 = 83
        hitsPeriod1Team2 = 87 
        hitsPeriod2Team1 = 95
        hitsPeriod2Team2 = 99
        hitsPeriod3Team1 = 107
        hitsPeriod3Team2 = 111
        # если случился овертайм, то может появиться новая строка в таблице бросков в створ и это собьёт индексы
        if response.xpath('//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()').extract()[50] == u'овертайм':
            blockedShotsPeriod1Team1 = 97
            blockedShotsPeriod1Team2 = 101
            blockedShotsPeriod2Team1 = 109
            blockedShotsPeriod2Team2 = 113
            blockedShotsPeriod3Team1 = 121
            blockedShotsPeriod3Team2 = 125
            hitsPeriod1Team1 = 99
            hitsPeriod1Team2 = 103 
            hitsPeriod2Team1 = 111
            hitsPeriod2Team2 = 115
            hitsPeriod3Team1 = 123
            hitsPeriod3Team2 = 127
            # если есть информация по броскам в створ в овертайме
            l.add_xpath('shotsOnGoalOvertimeTeam1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[54])
            l.add_xpath('shotsOnGoalOvertimeTeam2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[60])
        else:
            # иначе овертайма не было
            l.add_xpath('shotsOnGoalOvertimeTeam1', '0')
            l.add_xpath('shotsOnGoalOvertimeTeam2', '0')

        l.add_xpath('blockedShotsPeriod1Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[blockedShotsPeriod1Team1])
        l.add_xpath('blockedShotsPeriod1Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[blockedShotsPeriod1Team2])
        l.add_xpath('blockedShotsPeriod2Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[blockedShotsPeriod2Team1])
        l.add_xpath('blockedShotsPeriod2Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[blockedShotsPeriod2Team2])
        l.add_xpath('blockedShotsPeriod3Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[blockedShotsPeriod3Team1])
        l.add_xpath('blockedShotsPeriod3Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[blockedShotsPeriod3Team2])

        l.add_xpath('hitsPeriod1Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[hitsPeriod1Team1])
        l.add_xpath('hitsPeriod1Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[hitsPeriod1Team2])
        l.add_xpath('hitsPeriod2Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[hitsPeriod2Team1])
        l.add_xpath('hitsPeriod2Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[hitsPeriod2Team2])
        l.add_xpath('hitsPeriod3Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[hitsPeriod3Team1])
        l.add_xpath('hitsPeriod3Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer m-table_small")]/tbody//text()', lambda x: x[hitsPeriod3Team2])

        l.add_xpath('powerplayTimesTeam1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[6])
        l.add_xpath('powerplayTimesTeam2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[28])
        
        l.add_xpath('powerplayScoredTimesTeam1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[8])
        l.add_xpath('powerplayScoredTimesTeam2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[30])
        
        l.add_xpath('penaltykillTimesTeam1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[14])
        l.add_xpath('penaltykillTimesTeam2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[36])
        
        l.add_xpath('penaltykillAgainstTimesTeam1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[16])
        l.add_xpath('penaltykillAgainstTimesTeam2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[38])
        
        l.add_xpath('scored5vs5Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[51])
        l.add_xpath('scored5vs5Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[81])

        l.add_xpath('against5vs5Team1', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[81])
        l.add_xpath('against5vs5Team2', '//table[re:test(@class, "dataTable stripe compact row-border hl no-footer rc m-table_small")]/tbody//text()', lambda x: x[51])        
        
        l.add_value('url', response.url)

        # мы не всю информацию можем получить из протокола
        # общее количество бросков и количество вбрасываний необходимо получить
        # из текстовой трансляции
        textUrl = 'http://text.khl.ru/text/' + response.url.split('/')[5] + '.html'
        req = scrapy.Request(textUrl, callback=self.parse_text)
        req.meta['item'] = l
        yield req