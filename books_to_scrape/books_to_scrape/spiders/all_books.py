import scrapy
from csv import reader

class AllBooksSpider(scrapy.Spider):
    name = "all_books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = []

    with open('bookslinks.csv', 'r') as file:
            csv_reader = reader(file)
            for row in csv_reader:
                start_urls.append(row[0])
                break

    def parse(self, response):
        yield {
            'title': response.css('title::text').get(),
            'price': response.css('p.price_color::text').get(),
            'description': response.css('#content_inner > article > p::text').get(),
            'type': '',
            'UPC': '',
            'Availability': 'response.css('#content_inner > article > table > tr > td')[2].get()'
        }
