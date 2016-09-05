import scrapy

class Firstspider(scrapy.spiders.Spider):

    name = "firstspider"

    allowed_domains=["zhihu.com"]

    start_urls=["https://www.zhihu.com"]

    def parse(self,reponse):
        filename = reponse.url.split("/")[-2]
        with open(filename,"wb") as fget:
            f.write(reponse.body)
