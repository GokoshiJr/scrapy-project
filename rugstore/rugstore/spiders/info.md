# CSS selectors

scrapy shell https://www.therugshopuk.co.uk/rugs-by-type/rugs.html
cd rugstore - scrapy crawl allrugs

next_page = response.css('a[title=Next]::attr(href)').get()

all_products = response.css('div.product-item-info')

price = response.css('span.price::text').get()
link = response.css('a.product-item-link::attr(href)').get()
name = response.css('img.product-image-photo.image::attr(alt)').get()
