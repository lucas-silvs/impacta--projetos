import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    start_urls = ["http://imdb.com/chart/top/"]

    def parse(self, response):

        nomeFilmes = response.css('.titleColumn a::text').getall()

        anos = response.css('.secondaryInfo::text').getall()

        notas = response.css('strong::text').getall()

        listaFilmes=[]

        for i in range(250):
            filme = {
                "titulo": nomeFilmes[i],
                "ano": anos[i],
                "nota": notas[i]
            }
            listaFilmes.append(filme)

        # istaFilmes = {
        #     "nomeFilmes": nomeFilmes,
        #     "anos": anos,
        #     "notas": notas
        # }

        print(listaFilmes)
        return listaFilmes
