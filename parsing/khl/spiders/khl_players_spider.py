# -*- coding: utf-8 -*-

import re
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from khl.items import KhlPlayerItem
import json


class KhlPlayersLoader(XPathItemLoader):
    default_input_processor = MapCompose(lambda s: re.sub('\s+', ' ', s.strip()))
    default_output_processor = TakeFirst()


class KhlSpider(CrawlSpider):
    name = "khl_players"
    allowed_domains = ["khl.ru"]    
    start_urls = ["http://www.khl.ru/calendar/309/00/"] # календарь всех игр 2015-2016 сезона
    #start_urls = ["http://www.khl.ru/game/309/46649/protocol/"] # календарь всех игр 2015-2016 сезона

    rules = (
             Rule(SgmlLinkExtractor(allow=('/protocol')), callback='parse_item'),
             )
             
    id_pattern = re.compile("players/[0-9]+", re.IGNORECASE)
    name_pattern = re.compile("players/.*", re.IGNORECASE)
    
    goalkepeer = 'goalkepeer'
    defender = 'defender'
    forward = 'forward'
    
    def get_js_var(self, data):
        data_new = data[0].split("= ", 1)[1]
        data_new = data_new[:data_new.find(";") - 1]
        if (data_new[len(data_new) - 1]) == ',':
            data_new = data_new[:len(data_new) - 1]        
        data_new += ']' 
        return data_new
             
    def process(self, hxs, j, role, team, response):
        item = KhlPlayerItem()
        l = KhlPlayersLoader(item, hxs)
        l.add_xpath('id_match', '//span[re:test(@class, "e-num")]/text()')
        id = self.id_pattern.search(j[1]).group().split('/')[1]
        l.add_xpath('id', str(id))   
        name = self.name_pattern.search(j[1]).group().split('>')[1].split('<')[0]
        name = name.encode('utf-8') 
        l.add_value('name', name)        
        l.add_value('url', response.url)
        if role == self.goalkepeer: # для вратарей       
            l.add_value('shots_attemped', str(j[6]))
            l.add_value('goal_allowed', str(j[7]))
            l.add_value('shotout', str(j[13]))
            l.add_value('played_time', str(j[15]))
        else: # для нападающих и защитников
            l.add_value('goals', str(j[3]))
            l.add_value('asists', str(j[4]))
            l.add_value('plusminus', str(j[6]))
            l.add_value('penalty', str(j[7]))
            l.add_value('win_goals', str(j[12]))
            l.add_value('shots_on_goal', str(j[14]))
            l.add_value('faceoffs', str(j[16]))
            l.add_value('faceoffs_win', str(j[17]))
            l.add_value('hits', str(j[21]))
            l.add_value('shots_blocked', str(j[22]))
            l.add_value('played_time', str(j[19]))
        l.add_value('role', role)    
        l.add_value('team', str(team))
        return l.load_item()                 

    def parse_item(self, response):
        splited = response.url.split('game/')        
        if splited[1].startswith("309") == False: # если не весть каким образом оказались не в сезоне 2015-2016
            return        
        if "en" in response.url or "cn" in response.url:
            return
            
        hxs = HtmlXPathSelector(response)
        
        data_goalies_A = response.xpath('//script[contains(.,"var data_goalies_A")]/text()').re(".*var.*")
        data_goalies_B = response.xpath('//script[contains(.,"var data_goalies_B")]/text()').re(".*var.*")
        jsA = json.loads(self.get_js_var(data_goalies_A))
        jsB = json.loads(self.get_js_var(data_goalies_B))
        for j in jsA:
            yield self.process(hxs, j, self.goalkepeer, 1, response)
        for j in jsB:
            yield self.process(hxs, j, self.goalkepeer, 2, response)    
            
        data_defenses_A = response.xpath('//script[contains(.,"var data_defenses_A")]/text()').re(".*var.*")
        data_defenses_B = response.xpath('//script[contains(.,"var data_defenses_B")]/text()').re(".*var.*")
        jsA = json.loads(self.get_js_var(data_defenses_A))
        jsB = json.loads(self.get_js_var(data_defenses_B))
        for j in jsA:
            yield self.process(hxs, j, self.defender, 1, response)    
        for j in jsB:
            yield self.process(hxs, j, self.defender, 2, response)    
            
        data_forwards_A = response.xpath('//script[contains(.,"var data_forwards_A")]/text()').re(".*var.*")
        data_forwards_B = response.xpath('//script[contains(.,"var data_forwards_B")]/text()').re(".*var.*")
        jsA = json.loads(self.get_js_var(data_forwards_A))
        jsB = json.loads(self.get_js_var(data_forwards_B))
        for j in jsA:
            yield self.process(hxs, j, self.forward, 1, response)   
        for j in jsB:
            yield self.process(hxs, j, self.forward, 2, response)    

       # return l.load_item()