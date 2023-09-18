class SistemaDeGeracao:

    def __init__(self):
        self.geradores = []
        self.cargas = []
        return
    
    def adicionar_gerador(self,gerador):
        self.geradores.append(gerador)
        return
    
    def adicionar_carga(self, carga) :
        self.cargas.append(carga)
        return
    
    def balancear(self):
        consumo_total_de_energia = 0
        capacidade_atual_de_energia = 0
        sobrecarga = 0

        for carga in self.cargas:
            if carga.conectada == True:
                consumo_total_de_energia += carga.energia
        
        for gerador in self.geradores:
            capacidade_atual_de_energia += gerador.capacidade_atual

        sobrecarga = consumo_total_de_energia - capacidade_atual_de_energia;

        if sobrecarga > 0:
            print ("Sobrecarga detectada, balanceando geradores!")

            for gerador in self.geradores:
                
                if sobrecarga == 0:
                    print ("Sobrecarga estabilizada!")
                    break;
                
                capacidade_disponivel_no_gerador = gerador.capacidade_maxima - gerador.capacidade_atual

                if capacidade_disponivel_no_gerador > sobrecarga:
                    gerador.gerar(sobrecarga)
                    sobrecarga =  0;
                else:
                    gerador.gerar(capacidade_disponivel_no_gerador)
                    sobrecarga = sobrecarga - capacidade_disponivel_no_gerador