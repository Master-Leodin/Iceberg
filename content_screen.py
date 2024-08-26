import requests
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from bs4 import BeautifulSoup
import webbrowser

class BaseContentScreen(Screen):
    title = StringProperty("")
    image_source = StringProperty("")
    content = StringProperty("")
    podcast_url = StringProperty("")

    def load_content(self, url):
        try:
            self.title = ""
            self.image_source = ""
            self.content = "Carregando..."

            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            title_element = soup.find('h1')
            self.title = title_element.text if title_element else "Título não encontrado"

            image_element = soup.find('img')
            self.image_source = image_element['src'] if image_element else ""

            content_elements = soup.find_all('p')
            if content_elements:
                first_paragraph = content_elements[0].text[50:]
                penultimate_paragraph = content_elements[-2].text[:-50] if len(content_elements) > 1 else ""
                last_paragraph = content_elements[-1].text[:-50]

                paragraphs = [first_paragraph] + [p.text for p in content_elements[1:-2]] + [penultimate_paragraph, last_paragraph]
                self.content = "\n\n".join(paragraphs)
            else:
                self.content = "Conteúdo não encontrado"
        except Exception as e:
            self.title = "Erro ao carregar conteúdo"
            self.image_source = "data/sem_internet.png"
            self.content = "Sem internet ou erro do servidor"

    def set_podcast_url(self, url):
        self.podcast_url = url

    def open_podcast_fountain(self):
        if self.podcast_url:
            webbrowser.open(self.podcast_url)
        else:
            print("URL do podcast não definida.")

class ContentScreen_Criptozoologia(BaseContentScreen):
    pass

class ContentScreen_Criptozoologia_Provada(BaseContentScreen):
    pass

class ContentScreen_Mitologia(BaseContentScreen):
    pass

class ContentScreen_1_Grau(BaseContentScreen):
    pass

class ContentScreen_2_Grau(BaseContentScreen):
    pass

class ContentScreen_3_Grau(BaseContentScreen):
    pass

class ContentScreen_4_Grau(BaseContentScreen):
    pass

class ContentScreen_5_Grau(BaseContentScreen):
    pass

class ContentScreen_6_Grau(BaseContentScreen):
    pass

class ContentScreen_7_Grau(BaseContentScreen):
    pass

class ContentScreen_Desaparecimentos(BaseContentScreen):
    pass

class ContentScreen_Pessoas_Misteriosas(BaseContentScreen):
    pass

class ContentScreen_Viagem_No_Tempo(BaseContentScreen):
    pass

class ContentScreen_Lugares_Misteriosos(BaseContentScreen):
    pass

class ContentScreen_Ce(BaseContentScreen):
    pass

class ContentScreen_Falhas_Na_Matrix(BaseContentScreen):
    pass

class ContentScreen_Vivemos_Numa_Simulacao(BaseContentScreen):
    pass

class ContentScreen_Viagens_Para_Outra_Dimensao(BaseContentScreen):
    pass

class ContentScreen_Teorias_Da_Conspiracao(BaseContentScreen):
    pass

class ContentScreen_Artefatos_Misteriosos(BaseContentScreen):
    pass

class ContentScreen_Misterios_Da_Ciencia(BaseContentScreen):
    pass

class ContentScreen_Civilizacoes_Perdidas(BaseContentScreen):
    pass

class ContentScreen_Fenomenos_Paranormais(BaseContentScreen):
    pass

class ContentScreen_Casos_Nao_Resolvidos(BaseContentScreen):
    pass

class ContentScreen_Objetos_Amaldicoados(BaseContentScreen):
    pass

class ContentScreen_Mensagens_Criptografadas(BaseContentScreen):
    pass

class ContentScreen_Livros_Misteriosos(BaseContentScreen):
    pass

class ContentScreen_Reencarnacao(BaseContentScreen):
    pass
