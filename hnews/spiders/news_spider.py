import scrapy


class HNewsSpider(scrapy.Spider):
    name = "spidey"
    start_urls = [
        'http://news.ycombinator.com',
    ]

    def parse(self, response):
        for item in response.css('td.title'):
            yield {
                'text': item.css('a.storylink::text').get(),
                'link': item.css('a.storylink::attr(href)').get(),
            }
