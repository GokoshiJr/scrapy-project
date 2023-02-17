# CSS selectors

next_page = response.css('a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator::attr(href)').get()

all_products = response.css('div.s-main-slot.s-result-list.s-search-results.sg-row').get()

link = response.css('a.a-link-normal.s-no-outline::attr(href)').get()
name = response.css('img.s-image::attr(alt)').get()
price = response.css('span.a-offscreen').get().replace('£', '')
