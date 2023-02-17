import scrapy

BASE_URL = "https://www.amazon.co.uk"

class AllSweatersSpider(scrapy.Spider):
    name = "all_sweaters"
    allowed_domains = ["www.amazon.co.uk"]
    start_urls = ["https://www.amazon.co.uk/s?i=fashion-mens-clothing&srs=14704068031&rh=n%3A1731021031&content-id=amzn1.sym.d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pd_rd_r=976b2149-6fd3-42cd-aa0c-83605bbf9fcc&pd_rd_w=HGK8n&pd_rd_wg=6g5lZ&pf_rd_p=d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pf_rd_r=NS5TZZDMPGG13N6ZHRVH&qid=1675621985&ref=sr_pg_1%3E"]

    def parse(self, response):
        for item in response.css('div[data-component-type=s-search-result]'):
            yield {
                'title': item.css('img.s-image::attr(alt)').get(),
                'link': BASE_URL + item.css('a.a-link-normal.s-no-outline::attr(href)').get(),
                'price': item.css('span.a-offscreen::text').get()
            }

            """ next_page = response.css('a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse) """
