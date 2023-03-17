import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request

class PatentSpider(scrapy.Spider):
    name = "patent"
    start_urls = [
        "https://patents.google.com/patent/WO2007136468A2/en"
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 0.1,
        'RANDOMIZE_DOWNLOAD_DELAY': True,
        'CONCURRENT_REQUESTS': 200,
        'AUTOTHROTTLE_ENABLED': True,
        #'HTTPCACHE_ENABLED': True,
        #'HTTPCACHE_EXPIRATION_SECS': 86400,
        #'HTTPCACHE_DIR': 'httpcache'
    }

    def parse(self, response):
        self_link = response.request.url
        title = response.css('span[itemprop="title"]::text').get().strip()
        abstract = response.css('meta[name="description"]').xpath('@content').get().strip()
        number = response.css('title::text').get().split("-")[0].rstrip()
        publication_date = response.css('meta[name="DC.date"]').xpath('@content').get()
        inventors = response.css('dd[itemprop="inventor"]::text').getall()
        follow_links = response.xpath('//tbody/tr/td/a/@href').extract()

        yield {
            'self_link': self_link,
            'title': title,
            'abstract': abstract,
            'publication_number': number,
            'date': publication_date,
            'inventors': inventors
        }

        for link in follow_links:
            yield Request(url=response.urljoin(link), callback=self.parse)

def start_scraping():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "output.json": {"format": "json"}
        }
    })
    process.crawl(PatentSpider)
    process.start()

if __name__ == "__main__":
    start_scraping()
