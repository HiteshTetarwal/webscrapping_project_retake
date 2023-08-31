import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.http import FormRequest
from urllib.parse import urlparse
import pandas as pd
import time

class RunningSpider(scrapy.Spider):
    name = "players"
	
    custom_settings = {
        'FEEDS': {
            'items.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'overwrite': True,
            },
        },
    }

    def start_requests(self):
        self.start_time = time.time()
        start_urls = ["https://hoopshype.com/salaries/players/"]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.get_player_urls)

    def get_player_urls(self, response):
        links = response.xpath('//td[@class="name"]/a/@href').extract()
        limited_links = links[:101]  # Limiting to 100 links
        for link in limited_links:
            yield scrapy.Request(url=link, callback=self.get_data)

    def get_data(self, response):
        name = response.xpath('//div[@class="player-fullname"]/text()').get()
        if name:
            name = name.strip()

        team = response.xpath('//div[@class="player-team"]/a/text()').get()
        if team:
            team = team.strip()

        position = response.xpath('//span[@class="player-bio-text-line"]/b[text()="Position:"]/following-sibling::span[@class="player-bio-text-line-value"]/text()').get()
        born = response.xpath('//span[@class="player-bio-text-line"]/b[text()="Born:"]/following-sibling::span[@class="player-bio-text-line-value"]/text()').get()
        height = response.xpath('//span[@class="player-bio-text-line"]/b[text()="Height:"]/following-sibling::span[@class="player-bio-text-line-value"]/text()').get()
        weight = response.xpath('//span[@class="player-bio-text-line"]/b[text()="Weight:"]/following-sibling::span[@class="player-bio-text-line-value"]/text()').get()
        salary = response.xpath('//span[@class="player-bio-text-line"]/b[text()="Salary:"]/following-sibling::span[@class="player-bio-text-line-value"]/text()').get()

        # Print the extracted information
        print("Name:", name)
        print("Team:", team)
        print("Position:", position)
        print("Born:", born)
        print("Height:", height)
        print("Weight:", weight)
        print("Salary:", salary)
        print("--------------------------------")

        yield {
            'Name': name,
            'Team': team,
            'Position': position,
            'Born': born,
            'Height': height,
            'Weight': weight,
            'Salary': salary,
        }

    def closed(self, reason):
        end_time = time.time()
        runtime = end_time - self.start_time
        print(f"Spider runtime: {runtime:.2f} seconds")