from web_scraping import WebScraping
url = "https://g1.globo.com/"
web_scraping = WebScraping(url)

print(web_scraping.pick_all_news())