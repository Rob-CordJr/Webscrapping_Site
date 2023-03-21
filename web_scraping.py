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
        return self.soup.find_all('div', attrs={'class' : 'feed-post-body'})

    def __get_title(self, news):
        return news.find('div', attrs={'class' : '_evt'}).text
    
    def __get_link(self, news):
        return news.find('a').get('href')

    def __get_subtitle(self, news):
        valor_default = ''
        campo = news.find("div", attrs={'class' : 'feed-post-body-resumo'} )
        if campo is None:
            return valor_default
        return campo.text

    def __get_datetime(self, news):
        return news.find('span', attrs={'class' : 'feed-post-datetime'}).text

    def pick_all_news(self):
        for news in self.__get_news():
            titulo = self.__get_title(news)
            sub_titulo  = self.__get_subtitle(news)
            postagem =  self.__get_datetime(news)
            link = self.__get_link(news)
            if(titulo):
                print('Titulo:' ,titulo)
            if(sub_titulo):
                print('Sub-titulo:',sub_titulo)
            if(postagem):
                print('Postado a: ',postagem)
            if(link):
                print('Link da Reportagem: ',link)

            print('==================================')

            
         
            
