from web_scraping import WebScraping
url = "https://ge.globo.com/?utm_source=barraGCOM"
web_scraping = WebScraping(url)

print(web_scraping.pick_all_news())