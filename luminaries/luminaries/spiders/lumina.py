import scrapy

from scrapy import signals

class LuminaSpider(scrapy.Spider):
    name = "lumina"
    allowed_domains = ["lemanapro.ru"]
    start_urls = ['https://lemanapro.ru/catalogue/ulichnye-fonarnye-stolby']
    custom_settings = {
        'USER_AGENT': 'YandexBrowser/21.3.3.1000',
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': False
    }

    def parse(self, response):
        luminairies = response.css('div.p155f0re_plp')
        for luminaire in luminairies:
            yield {
                'name': luminaire.css('div.p1h8lbu4_plp span::text').get(),
                'price': luminaire.css('div.mvc4syb_plp span::text').get(),
                'url': luminaire.css('a').attrib['href']
            }

