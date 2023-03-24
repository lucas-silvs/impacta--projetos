import scrapy

# Arthur Vinicius Santos Silva RA: 1903665
# Larissa Ionafa RA: 1903166
# Lucas da Silva Santos RA: 1904209
# Rafael Serino Kiss RA: 1903107

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/catalogue/category/books/romance_8/index.html", \
                   "http://books.toscrape.com/catalogue/category/books/travel_2/index.html", \
                    "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"]

    def parse(self, response):
        categoria = response.css('h1::text').get()

        for livros in response.css(".col-lg-3 "):            
                    yield {
                        "categoria": categoria,
                        "Titulo": livros.css('.col-lg-3 a::text').get(),
                        "preco" : livros.css('.col-lg-3 .price_color::text').get(),
                        "estoque": livros.css(".availability").get().split("\n")[3].strip()      
                    }
        pass
