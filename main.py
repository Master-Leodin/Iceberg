from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.animation import Animation
from content_screen import (ContentScreen_Criptozoologia,
ContentScreen_Criptozoologia_Provada,
ContentScreen_Mitologia,
ContentScreen_Ce,
ContentScreen_1_Grau,
ContentScreen_2_Grau,
ContentScreen_3_Grau,
ContentScreen_4_Grau,
ContentScreen_5_Grau,
ContentScreen_6_Grau,
ContentScreen_7_Grau,
ContentScreen_Falhas_Na_Matrix,
ContentScreen_Vivemos_Numa_Simulacao,
ContentScreen_Desaparecimentos,
ContentScreen_Viagem_No_Tempo,
ContentScreen_Pessoas_Misteriosas,
ContentScreen_Viagens_Para_Outra_Dimensao,
ContentScreen_Lugares_Misteriosos,
ContentScreen_Teorias_Da_Conspiracao,
ContentScreen_Artefatos_Misteriosos,
ContentScreen_Misterios_Da_Ciencia,
ContentScreen_Civilizacoes_Perdidas,
ContentScreen_Fenomenos_Paranormais,
ContentScreen_Casos_Nao_Resolvidos,
ContentScreen_Objetos_Amaldicoados,
ContentScreen_Mensagens_Criptografadas,
ContentScreen_Livros_Misteriosos,
ContentScreen_Reencarnacao

)



# Carregar os arquivos KV
Builder.load_file('main.kv')
Builder.load_file('padroes.kv')
Builder.load_file('assuntos/animais.kv')
Builder.load_file('assuntos/lugares_misteriosos.kv')
Builder.load_file('assuntos/pessoas.kv')
Builder.load_file('assuntos/ufologia.kv')
Builder.load_file('assuntos/livros.kv')
Builder.load_file('assuntos/teorias_da_conspiracao.kv')
Builder.load_file('contents/content_lugares/content_screen_lugares_misteriosos.kv')
Builder.load_file('contents/content_teorias_da_conspiracao/content_screen_teorias_da_conspiracao.kv')
Builder.load_file('assuntos/artefatos_misteriosos.kv')
Builder.load_file('contents/content_artefatos_misteriosos/content_screen_artefatos_misteriosos.kv')
Builder.load_file('assuntos/misterios_da_ciencia.kv')
Builder.load_file('contents/content_misterios_da_ciencia/content_screen_misterios_da_ciencia.kv')
Builder.load_file('assuntos/civilizacoes_perdidas.kv')
Builder.load_file('contents/content_civilizacoes_perdidas/content_screen_civilizacoes_perdidas.kv')
Builder.load_file('assuntos/fenomenos_paranormais.kv')
Builder.load_file('contents/content_fenomenos_paranormais/content_screen_fenomenos_paranormais.kv')
Builder.load_file('assuntos/casos_nao_resolvidos.kv')
Builder.load_file('contents/content_casos_nao_resolvidos/content_screen_casos_nao_resolvidos.kv')
Builder.load_file('assuntos/objetos_amaldicoados.kv')
Builder.load_file('contents/content_objetos_amaldicoados/content_screen_objetos_amaldicoados.kv')
Builder.load_file('assuntos/mensagens_criptografadas.kv')
Builder.load_file('contents/content_mensagens_criptografadas/content_screen_mensagens_criptografadas.kv')
Builder.load_file('assuntos/livros_misteriosos.kv')
Builder.load_file('contents/content_livros_misteriosos/content_screen_livros_misteriosos.kv')
Builder.load_file('assuntos/reencarnacao.kv')
Builder.load_file('contents/content_reencarnacao/content_screen_reencarnacao.kv')
Builder.load_file('contents/content_ufologia/content_screen_ce.kv')
Builder.load_file('ufologia/ufologia_1_grau.kv')
Builder.load_file('ufologia/ufologia_2_grau.kv')
Builder.load_file('ufologia/ufologia_3_grau.kv')
Builder.load_file('ufologia/ufologia_4_grau.kv')
Builder.load_file('ufologia/ufologia_5_grau.kv')
Builder.load_file('ufologia/ufologia_6_grau.kv')
Builder.load_file('ufologia/ufologia_7_grau.kv')
Builder.load_file('contents/content_ufologia/content_screen_1_grau.kv')
Builder.load_file('contents/content_ufologia/content_screen_2_grau.kv')
Builder.load_file('contents/content_ufologia/content_screen_3_grau.kv')
Builder.load_file('contents/content_ufologia/content_screen_4_grau.kv')
Builder.load_file('contents/content_ufologia/content_screen_5_grau.kv')
Builder.load_file('contents/content_ufologia/content_screen_6_grau.kv')
Builder.load_file('contents/content_ufologia/content_screen_7_grau.kv')
Builder.load_file('assuntos/falhas_na_matrix.kv')
Builder.load_file('contents/content_falhas_na_matrix/content_screen_falhas_na_matrix.kv')
Builder.load_file('assuntos/vivemos_numa_simulacao.kv')
Builder.load_file('contents/content_vivemos_numa_simulacao/content_screen_vivemos_numa_simulacao.kv')
Builder.load_file('pessoas/viagem_no_tempo.kv')
Builder.load_file('pessoas/pessoas_misteriosas.kv')
Builder.load_file('pessoas/desaparecimentos.kv')
Builder.load_file('pessoas/viagens_para_outra_dimensao.kv')
Builder.load_file('contents/content_pessoas/content_screen_viagem_no_tempo.kv')
Builder.load_file('contents/content_pessoas/content_screen_pessoas_misteriosas.kv')
Builder.load_file('contents/content_pessoas/content_screen_desaparecimentos.kv')
Builder.load_file('contents/content_pessoas/content_screen_viagens_para_outra_dimensao.kv')
Builder.load_file('animais/criptozoologia.kv')
Builder.load_file('animais/criptozoologia_provada.kv')
Builder.load_file('animais/mitologia.kv')
Builder.load_file('contents/content_animais/content_screen_criptozoologia.kv')
Builder.load_file('contents/content_animais/content_screen_criptozoologia_provada.kv')
Builder.load_file('contents/content_animais/content_screen_mitologia.kv')
Builder.load_file('assuntos/contato.kv')

class GerenciadorTelas(ScreenManager):
    pass
class Principal(Screen):
    pass
class Animais(Screen):
    pass
class Ufologia(Screen):
    pass
class Ufologia_1_Grau(Screen):
    pass
class Ufologia_2_Grau(Screen):
    pass
class Ufologia_3_Grau(Screen):
    pass
class Ufologia_4_Grau(Screen):
    pass
class Ufologia_5_Grau(Screen):
    pass
class Ufologia_6_Grau(Screen):
    pass
class Ufologia_7_Grau(Screen):
    pass
class Falhas_Na_Matrix(Screen):
    pass
class Vivemos_Numa_Simulacao(Screen):
    pass
class Pessoas(Screen):
    pass
class Viagem_No_Tempo(Screen):
    pass
class Pessoas_Misteriosas(Screen):
    pass
class Desaparecimentos(Screen):
    pass
class Viagens_Para_Outra_Dimensao(Screen):
    pass
class Lugares_Misteriosos(Screen):
    pass
class Criptozoologia(Screen):
    pass
class Criptozoologia_Provada(Screen):
    pass
class Mitologia(Screen):
    pass
class Teorias_Da_Conspiracao(Screen):
    pass
class Artefatos_Misteriosos(Screen):
    pass
class Misterios_Da_Ciencia(Screen):
    pass
class Civilizacoes_Perdidas(Screen):
    pass
class Fenomenos_Paranormais(Screen):
    pass
class Casos_Nao_Resolvidos(Screen):
    pass
class Objetos_Amaldicoados(Screen):
    pass
class Mensagens_Criptografadas(Screen):
    pass
class Livros_Misteriosos(Screen):
    pass
class Reencarnacao(Screen):
    pass
class Contato(Screen):
    pass

# LIVROS PARA VENDA COMISSIONADA
class Livros(Screen):
    pass

class Gerenciador(App):
    def on_start(self):
        botao_sobre = self.root.get_screen('principal').ids.get('botao_sobre')
        if botao_sobre:
            self.animate_button_text(botao_sobre)

    def animate_button_text(self, widget):
        animText = Animation(color=(0, 0, 0, 1), duration=0.5) + Animation(color=(0, 1, 0, 1), duration=3) + Animation(color=(0, 0, 0, 1), duration=0.5) + Animation(color=(1, 0.5, 0.5, 1), duration=3) + Animation(color=(0, 0, 0, 1), duration=0.5) + Animation(color=(0, 0, 1, 1), duration=3)
        animText.repeat = True
        animText.start(widget)

    def build(self):
        Window.maximize()

        sm = GerenciadorTelas()
        sm.add_widget(Principal(name='principal'))

        sm.add_widget(Ufologia(name='ufologia'))

        sm.add_widget(ContentScreen_Ce(name='content_screen_ce'))

        sm.add_widget(Ufologia_1_Grau(name='ufologia_1_grau'))
        sm.add_widget(ContentScreen_1_Grau(name='content_screen_1_grau'))

        sm.add_widget(Ufologia_2_Grau(name='ufologia_2_grau'))
        sm.add_widget(ContentScreen_2_Grau(name='content_screen_2_grau'))

        sm.add_widget(Ufologia_3_Grau(name='ufologia_3_grau'))
        sm.add_widget(ContentScreen_3_Grau(name='content_screen_3_grau'))

        sm.add_widget(Ufologia_4_Grau(name='ufologia_4_grau'))
        sm.add_widget(ContentScreen_4_Grau(name='content_screen_4_grau'))

        sm.add_widget(Ufologia_5_Grau(name='ufologia_5_grau'))
        sm.add_widget(ContentScreen_5_Grau(name='content_screen_5_grau'))

        sm.add_widget(Ufologia_6_Grau(name='ufologia_6_grau'))
        sm.add_widget(ContentScreen_6_Grau(name='content_screen_6_grau'))

        sm.add_widget(Ufologia_7_Grau(name='ufologia_7_grau'))
        sm.add_widget(ContentScreen_7_Grau(name='content_screen_7_grau'))

        sm.add_widget(Vivemos_Numa_Simulacao(name='vivemos_numa_simulacao'))
        sm.add_widget(ContentScreen_Vivemos_Numa_Simulacao(name='content_screen_vivemos_numa_simulacao'))

        sm.add_widget(Pessoas(name='pessoas'))

        sm.add_widget(Desaparecimentos(name='desaparecimentos'))
        sm.add_widget(ContentScreen_Desaparecimentos(name='content_screen_desaparecimentos'))

        sm.add_widget(Viagem_No_Tempo(name='viagem_no_tempo'))
        sm.add_widget(ContentScreen_Viagem_No_Tempo(name='content_screen_viagem_no_tempo'))

        sm.add_widget(Pessoas_Misteriosas(name='pessoas_misteriosas'))
        sm.add_widget(ContentScreen_Pessoas_Misteriosas(name='content_screen_pessoas_misteriosas'))

        sm.add_widget(Viagens_Para_Outra_Dimensao(name='viagens_para_outra_dimensao'))
        sm.add_widget(ContentScreen_Viagens_Para_Outra_Dimensao(name='content_screen_viagens_para_outra_dimensao'))

        sm.add_widget(Lugares_Misteriosos(name='lugares_misteriosos'))
        sm.add_widget(ContentScreen_Lugares_Misteriosos(name='content_screen_lugares_misteriosos'))

        sm.add_widget(Animais(name='animais'))

        sm.add_widget(Criptozoologia(name='criptozoologia'))
        sm.add_widget(ContentScreen_Criptozoologia(name='content_screen_criptozoologia'))

        sm.add_widget(Criptozoologia_Provada(name='criptozoologia_provada'))
        sm.add_widget(ContentScreen_Criptozoologia_Provada(name='content_screen_criptozoologia_provada'))

        sm.add_widget(Mitologia(name='mitologia'))
        sm.add_widget(ContentScreen_Mitologia(name='content_screen_mitologia'))

        sm.add_widget(Falhas_Na_Matrix(name='falhas_na_matrix'))
        sm.add_widget(ContentScreen_Falhas_Na_Matrix(name='content_screen_falhas_na_matrix'))

        sm.add_widget(Teorias_Da_Conspiracao(name='teorias_da_conspiracao'))
        sm.add_widget(ContentScreen_Teorias_Da_Conspiracao(name='content_screen_teorias_da_conspiracao'))
        
        sm.add_widget(Artefatos_Misteriosos(name='artefatos_misteriosos'))
        sm.add_widget(ContentScreen_Artefatos_Misteriosos(name='content_screen_artefatos_misteriosos'))
        
        sm.add_widget(Misterios_Da_Ciencia(name='misterios_da_ciencia'))
        sm.add_widget(ContentScreen_Misterios_Da_Ciencia(name='content_screen_misterios_da_ciencia'))
        
        sm.add_widget(Civilizacoes_Perdidas(name='civilizacoes_perdidas'))
        sm.add_widget(ContentScreen_Civilizacoes_Perdidas(name='content_screen_civilizacoes_perdidas'))
        
        sm.add_widget(Fenomenos_Paranormais(name='fenomenos_paranormais'))
        sm.add_widget(ContentScreen_Fenomenos_Paranormais(name='content_screen_fenomenos_paranormais'))
        
        sm.add_widget(Casos_Nao_Resolvidos(name='casos_nao_resolvidos'))
        sm.add_widget(ContentScreen_Casos_Nao_Resolvidos(name='content_screen_casos_nao_resolvidos'))
        
        sm.add_widget(Objetos_Amaldicoados(name='objetos_amaldicoados'))
        sm.add_widget(ContentScreen_Objetos_Amaldicoados(name='content_screen_objetos_amaldicoados'))
        
        sm.add_widget(Mensagens_Criptografadas(name='mensagens_criptografadas'))
        sm.add_widget(ContentScreen_Mensagens_Criptografadas(name='content_screen_mensagens_criptografadas'))
        
        sm.add_widget(Livros_Misteriosos(name='livros_misteriosos'))
        sm.add_widget(ContentScreen_Livros_Misteriosos(name='content_screen_livros_misteriosos'))
        
        sm.add_widget(Reencarnacao(name='reencarnacao'))
        sm.add_widget(ContentScreen_Reencarnacao(name='content_screen_reencarnacao'))
        
        sm.add_widget(Contato(name='contato'))

# LIVROS PARA VENDA COMISSIONADA        
        sm.add_widget(Livros(name='livros'))
        
        return sm

Gerenciador().run()
