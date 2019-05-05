import scrapy


class HNewsSpider(scrapy.Spider):
    name = "spidey"
    start_urls = [
        'https://news.ycombinator.com/',
    ]

    def parse(self, response):
        for item in response.css('tr.athing'):
            yield {
                'text': item.css('a.storylink::text').get(),
                'link': item.css('a.storylink::attr(href)').get(),
            }
        next_page = response.css('td.title a.morelink::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
