from bs4 import BeautifulSoup
import requests


class WebScraping:
    # Construtor da classe principal
    def __init__(self, url):
        self.url = url
        self.soup = self.__get_html()
    # Metodo que retorna os elementos do documento da pagina web

    def __get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def __get_news(self):
        return self.soup.find_all("div", class_="_evt")

    def __get_title(self, news):
        return news.find("a", class_="feed-post-link gui-color-primary gui-color-hover").text

    def __get_subtitle(self, news):
        valor_default = ''
        campo = news.find("span", class_="feed-post-header-chapeu")
        if campo is None:
            return valor_default
        return campo.text

    def __get_datetime(self, news):
        valor_default = ''
        campo = news.find("span", class_="feed-post-datetime")
        if campo is None:
            return valor_default
        return campo.text

    def pick_all_news(self):
        for news in self.__get_news():
            news_info = {}
            news_info["Titulo"] = self.__get_subtitle(news)
            news_info["Legenda"] = self.__get_title(news)
            news_info["Postado a:"] = self.__get_datetime(news)
            print(news_info)
            
