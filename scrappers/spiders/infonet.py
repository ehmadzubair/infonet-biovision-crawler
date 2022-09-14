from scrapy.spiders import CrawlSpider, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import Rule


def clean(lst_or_str):
    if not lst_or_str:
        return

    if not isinstance(lst_or_str, list):
        return lst_or_str.strip()

    return [txt.strip() for txt in lst_or_str if txt.strip()]


class InfonetSpider(CrawlSpider):
    name = 'infonet'
    allowed_domains = ['infonet-biovision.org']
    # start_urls = ['https://infonet-biovision.org/crops-fruits-veg']
    start_urls = [
        'https://infonet-biovision.org/PlantHealth/Pests/African-armyworm'
    ]

    rules = (
        Rule(LinkExtractor(restrict_css=".views-fluid-grid li .field-content"), callback="parse_product"),
    )

    def start_requests(self):
        requests = []
        for url in self.start_urls:
            requests.append(Request(url, callback=self.parse_product))
        return requests

    def parse_product(self, response):
        return {
            "url": response.url,
            "name": self.product_name(response),
            # "pest_and_diseases": self.parse_pest_and_diseases(response),
            "hots_plants": self.parse_host_plants(response),
            "images": self.parse_images(response),
            # "pest_information": self.parse_pest_information(response),
            "html": self.parse_html(response)
        }

    def product_name(self, response):
        return clean(response.css(".pane-content h1::text").get())

    def product_content(self, response):
        headings = clean(response.css("#simple-table-of-contents li a::text").getall())
        content_ids = clean(response.css("#simple-table-of-contents li a::attr(href)").getall())
        # content = [
        #     response.xpath(f'//h2[contains(@id, "{content_id.replace("#", "")}")]/..').getall()
        #     for content_id in content_ids
        # ]
        content = []
        for content_id in content_ids:
            _content = response.xpath(f'//h2[contains(@id, "{content_id.replace("#", "")}")]/..').getall()
            content.append(_content)

        return dict(zip(headings, content))

    def parse_pest_and_diseases(self, response):
        keys = clean(response.css(".pane-ph-minor-pest-list-panel-pane-1 .views-row span::text").getall())
        values = clean(response.css(".pane-ph-minor-pest-list-panel-pane-1 .views-row a::attr(href)").getall())
        return dict(zip(keys, values))


    def parse_host_plants(self, response):
        keys = clean(response.css(".pane-node-field-host-plants .node ::text").getall())
        values = clean(response.css(".pane-node-field-host-plants .textformatter-list a::attr(href)").getall())
        return dict(zip(keys, values))

    def parse_images(self, response):
        return clean(
            response.css(
                ".panels-flexible-row-plant_health_layout_-3 .jcarousel-skin-tango img::attr(src)"
            ).getall()
        )

    def parse_pest_information(self, response):
        pest_information = []
        for info in response.css(".pane-final-phcfv-datasheet-pests-panel-pane-1 form>div>div.views-row"):
            details = {
                "title": clean(" ".join(info.css(".tt-description p:nth-child(2) a ::text").getall())),
                "description": clean(" ".join(info.css(".tt-description p:not(p:nth-child(2)) ::text").getall())),
                "what_to_do": clean(info.css(".tt-to-do-text li ::text").getall()),
                "images": clean(info.css("img::attr(src)").getall())
            }
            pest_information.append(details)
        return pest_information

    def parse_html(self, response):
        return response.css("#block-system-main>.panel-flexible .datasheet-content>.inside").getall()

    def parse_biological_pest_control(self, response):
        pest_information = []
        for info in response.css(".pane-final-phcfv-datasheet-pests-panel-pane-1 form>div>div.views-row"):
            details = {
                "title": clean(" ".join(info.css(".tt-description p:nth-child(2) a ::text").getall())),
                "description": clean(" ".join(info.css(".tt-description p:not(p:nth-child(2)) ::text").getall())),
                "what_to_do": clean(info.css(".tt-to-do-text li ::text").getall()),
                "images": clean(info.css("img::attr(src)").getall())
            }
            pest_information.append(details)
        return pest_information

    # def parse(self, response, **kwargs):
    #     yield from super().parse(response)
        # return {"url": response.url}
