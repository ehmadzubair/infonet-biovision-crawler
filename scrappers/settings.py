# Scrapy settings for scrappers project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrappers'

SPIDER_MODULES = ['scrappers.spiders']
NEWSPIDER_MODULE = 'scrappers.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrappers (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'authority': 'www.upwork.com',
#   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#   'accept-language': 'en-GB;q=0.8',
#   'cache-control': 'max-age=0',
#   'cookie': '_pxhd=FMMpqBQvHmvjrBuy8P7ONObUhqZyMtPs8UcXv2DuwpCtmAHJCj/OF-1za6LEYEvRnj7yfpVcgbN9vLgwbJVFrw==:OEtIpyxTCxKIhnRSrYj3zrjYgSZSWm2C99sPAhkWn2XgdiCR3Uny63P51dEmbV6O7OH4551yB3NvZNiGAYzpvySLXKtJoOP6/8uizyVDkms=; visitor_id=144.48.135.58.1661766985487000; lang=en; cookie_prefix=; cookie_domain=.upwork.com; __cf_bm=1WJjyBIiqLKcDrI2TIFax1hSRdxv3SfDKNbjsiH3weI-1661766985-0-AXv+Kf1JA0GiKHmxG0YF4aGNWj8OjRNJtEOQoNCc6sLrDhRcM8HymazU/xXE6Ymy7uNkBWd6Mexfcl6Zp+0b5Gg=; __cfruid=4cce73c525d33891e4fa179b07359a4efb16f926-1661766985; device_view=full; _sp_ses.2a16=*; _gcl_au=1.1.1957977324.1661766988; G_ENABLED_IDPS=google; _fbp=fb.1.1661767013887.1114311061; emulatemq=%7B%22breakpoint%22%3A%22xl%22%2C%22size%22%3A%221200%22%2C%22sizes%22%3A%7B%22xs%22%3A0%2C%22sm%22%3A480%2C%22md%22%3A768%2C%22lg%22%3A992%2C%22xl%22%3A1200%7D%2C%22mobile%22%3Afalse%2C%22desktop%22%3Atrue%7D; _sp_id.2a16=565e355e-4cc6-430e-81cf-ab7f70daba3f.1661766987.1.1661767077.1661766987.756d95cc-be8a-4425-a418-03d5ddba7948; OptanonConsent=isGpcEnabled=1&datestamp=Mon+Aug+29+2022+14%3A57%3A57+GMT%2B0500+(Pakistan+Standard+Time)&version=6.39.0&isIABGlobal=false&hosts=&consentId=8ad4dfed-e6d8-4289-b677-8aed2896c1a9&interactionCount=1&landingPath=https%3A%2F%2Fwww.upwork.com%2Ffreelancers%2F~01f07591bd4eab0533%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A1%2CC0004%3A0; XSRF-TOKEN=a830c35a4f92142db6451523e8e894ab; AWSALB=Kdvi9/O+7y9zJ4VxZ0r8xs/2sdOc9mQlaaPE60MGGh6G2lPqnCPy65TKrIEKicusyxK+88mlMaWBUadOem1HQlzBcJwQ2ofCfyJFkPqUIg2qlZibHNUTzKclxhRA; AWSALBCORS=Kdvi9/O+7y9zJ4VxZ0r8xs/2sdOc9mQlaaPE60MGGh6G2lPqnCPy65TKrIEKicusyxK+88mlMaWBUadOem1HQlzBcJwQ2ofCfyJFkPqUIg2qlZibHNUTzKclxhRA; spt=445a01ed-6bed-4463-a30a-733c090d1a25; enabled_ff=!CI10270Air2Dot5QTAllocations,!CI10857Air3Dot0,CI11132Air2Dot75,!air2Dot76,OTBnrOn,air2Dot76Qt,!CI12577UniversalSearch,!SSINav,!SFE701ProfileSliderV2,!SFE604UFSSortPriceFilter,CI9570Air2Dot5; XSRF-TOKEN=68c7056d49475ae15a593f17427808cc; __cf_bm=7UtvI95ABNm4u8AryTfL6Oow7wQ7haqalNJkytqP_Nk-1661768008-0-AQGe9IU/UDbRSWmbCiNQT4s6ERxGpSuTHmguZQ7jzZWewwXitZtrbQ++OZyB/CXlMAO8ETmZBpCpC5O23B5JmT4=; __cfruid=599b87a3f932f2c1b14ceafd56ed5c694a4c9044-1660816398; company_last_accessed=d7380788; current_organization_uid=572458888381280257; visitor_id=144.48.135.58.1654851668596000; _pxhd=7a3pbipOF9h8iHrHt0JPiT7AF1Cwgh/sQA0IwOv3Qz0waop-L3Hg5DnUlqoZiE7xEdW6egYti0cJp0EyrCuYjA==:Penn-orvqxEw3X6PLTuG1au/hFVH33ykw04m9etOmfJln19cISqQ/3K3GWYMZFE/emMHI7/cdPu8VM2uGkzlFiQmEFHrypjPjKWBltuWyEw=; enabled_ff=OTBnrOn,CI11132Air2Dot75,!air2Dot76,CI9570Air2Dot5,air2Dot76Qt,SSINav,!CI10270Air2Dot5QTAllocations,!CI12577UniversalSearch,!CI10857Air3Dot0',
#   'if-none-match': 'W/"a821b-6b4ibuHw8+DN8wQ7ITAWA3ySbnA"',
#   'referer': 'https://www.upwork.com/freelancers/~01f07591bd4eab0533/',
#   'sec-fetch-dest': 'document',
#   'sec-fetch-mode': 'navigate',
#   'sec-fetch-site': 'same-origin',
#   'sec-fetch-user': '?1',
#   'sec-gpc': '1',
#   'upgrade-insecure-requests': '1',
#   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrappers.middlewares.ScrappersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrappers.middlewares.ScrappersDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrappers.pipelines.ScrappersPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
