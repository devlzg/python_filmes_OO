from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @abstractmethod
    def __str__(self):
        pass
        
    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self) -> str:
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes"

class Playlist:
    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas
        
    def __getitem__ (self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
        
vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
tmep = Filme("todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)
mandalorian = Serie("The Mandalorian", 2019, 3)

tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep, mandalorian]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {playlist_fim_de_semana}")
for programa in playlist_fim_de_semana: 
    print(programa)

print(f"Tá ou não tá? {demolidor in playlist_fim_de_semana}")