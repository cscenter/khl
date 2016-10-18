# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
from khl.items import KhlItem
import inspect

class CSVPipeline(object):

  def __init__(self):
    self.files = {}

  @classmethod
  def from_crawler(cls, crawler):
    pipeline = cls()
    crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    return pipeline

  def spider_opened(self, spider):
    file = open('%s_items.csv' % spider.name, 'w+b')
    self.files[spider] = file
    self.exporter = CsvItemExporter(file)
    # определяем порядок следования в csv файле
    self.exporter.fields_to_export = [
    'id',
    'timestamp',
    'team1Name',
    'team2Name',
    'score',
    'referees',
    'linesmen',
    'coachTeam1',
    'coachTeam2',
    'shotsPeriod1Team1',
    'shotsPeriod1Team2',
    'shotsPeriod2Team1',
    'shotsPeriod2Team2',
    'shotsPeriod3Team1',
    'shotsPeriod3Team2',
    'shotsOnGoalPeriod1Team1',
    'shotsOnGoalPeriod1Team2',
    'shotsOnGoalPeriod2Team1',
    'shotsOnGoalPeriod2Team2',
    'shotsOnGoalPeriod3Team1',
    'shotsOnGoalPeriod3Team2',
    'shotsOnGoalOvertimeTeam1',
    'shotsOnGoalOvertimeTeam2',
    'blockedShotsPeriod1Team1',
    'blockedShotsPeriod1Team2',
    'blockedShotsPeriod2Team1',
    'blockedShotsPeriod2Team2',
    'blockedShotsPeriod3Team1',
    'blockedShotsPeriod3Team2',
    'hitsPeriod1Team1',
    'hitsPeriod1Team2',
    'hitsPeriod2Team1',
    'hitsPeriod2Team2',
    'hitsPeriod3Team1',
    'hitsPeriod3Team2',
    'faceoffsWonPeriod1Team1',
    'faceoffsWonPeriod1Team2',
    'faceoffsWonPeriod2Team1',
    'faceoffsWonPeriod2Team2',
    'faceoffsWonPeriod3Team1',
    'faceoffsWonPeriod3Team2',
    'powerplayTimesTeam1',
    'powerplayTimesTeam2',
    'powerplayScoredTimesTeam1',
    'powerplayScoredTimesTeam2',
    'penaltykillTimesTeam1',
    'penaltykillTimesTeam2',
    'penaltykillAgainstTimesTeam1',
    'penaltykillAgainstTimesTeam2',
    'scored5vs5Team1',
    'scored5vs5Team2',
    'against5vs5Team1',
    'against5vs5Team2',
    'url'
    ]
    self.exporter.start_exporting()

  def spider_closed(self, spider):
    self.exporter.finish_exporting()
    file = self.files.pop(spider)
    file.close()

  def process_item(self, item, spider):
    self.exporter.export_item(item)
    return item
