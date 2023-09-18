class Gerador:
    
    def __init__(self, nome, capacidade_maxima):
        self.nome = nome;
        self.capacidade_maxima = capacidade_maxima;
        self.capacidade_atual = 0;
        
        return

    def gerar(self, energia):
      self.capacidade_atual += energia
      return
    
    def desligar(self):
      self.capacidade_atual = 0
      return