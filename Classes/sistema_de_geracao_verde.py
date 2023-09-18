from Classes.sistema_de_geracao import SistemaDeGeracao
class SistemaDeGeracaoVerde(SistemaDeGeracao):

    def __init__(self):
        super().__init__()
        self.cargas_desconectadas = []
        return
    
    def adicionar_gerador(self, gerador):
        super().adicionar_gerador(gerador)

        if gerador.tipo_geracao != "termelétrica":
            self.desconectar_geradores("termelétrica")

        self.conectar_todas_as_cargas()
        self.balancear()

    def desconectar_geradores(self, tipo):
        for gerador in self.geradores:
            if gerador.tipo_geracao == tipo:
                gerador.desligar()
        return
    
    def adicionar_carga(self, carga) :
        super().adicionar_carga(carga)
        carga.conectar()
        self.balancear()
        return

    def desconectar_cargas(self):
        for carga in self.cargas:
            if carga.conectada == True:
                carga.desconectar()
        return
         
    def conectar_todas_as_cargas(self):
        for carga in self.cargas:
            if carga.conectada == False:
                for carga_desconectada in self.cargas_desconectadas:
                    if  carga_desconectada == carga:
                        self.cargas_desconectadas.remove(carga_desconectada)
                carga.conectar()
        return   

    def listar_cargas_desconectadas(self):
        for carga in self.cargas_desconectadas:
            print(f"{carga.nome} {carga.energia}")
        return   
           
    def balancear(self):
        consumo_total_de_energia = 0
        capacidade_maxima_de_energia = 0
        capacidade_atual_de_energia = 0
        sobrecarga = 0

        if len(self.geradores) == 0:
            self.desconectar_cargas()
            print("Nenhum gerador disponível.")
            return

        for carga in self.cargas:
            if carga.conectada == True:
                consumo_total_de_energia += carga.energia
        
        for gerador in self.geradores:
            capacidade_maxima_de_energia += gerador.capacidade_maxima
            capacidade_atual_de_energia += gerador.capacidade_atual

        sobrecarga = consumo_total_de_energia - capacidade_atual_de_energia;

        if capacidade_atual_de_energia == capacidade_maxima_de_energia and sobrecarga > 0:
            while(True):

                print(f"Geradores em capacidade Máxima, Sobrecarga detectada, Desligando cargas excedentes!")

                cargas_ativas_ordenadas_por_energia = sorted([carga for carga in self.cargas if carga.conectada], key=lambda carga: carga.energia, reverse=True)
                carga = cargas_ativas_ordenadas_por_energia[-1]
                carga.desconectar()

                sobrecarga -= carga.energia
                consumo_total_de_energia -= carga.energia

                self.cargas_desconectadas.append(carga)

                if(consumo_total_de_energia <= capacidade_maxima_de_energia):
                    print("Todas as Cargas excedentes foram removidas")
                    break

        if sobrecarga > 0:

            print (f"Sobrecarga detectada, balanceando geradores!")

            geradores_ordenados_por_custo_e_tipo = sorted(self.geradores, key=lambda gerador: (gerador.tipo_geracao == "termelétrica", gerador.custo_mw))
            quantidade_total_geradores = len(geradores_ordenados_por_custo_e_tipo);
            geradores_analisados = 0;

            for gerador in geradores_ordenados_por_custo_e_tipo:
                
                geradores_analisados += 1

                if sobrecarga == 0:
                    print(  f"Sobrecarga estabilizada!")
                    break

                capacidade_disponivel_no_gerador = gerador.capacidade_maxima - gerador.capacidade_atual

                if capacidade_disponivel_no_gerador > 0:

                    if capacidade_disponivel_no_gerador > sobrecarga:
                        gerador.gerar(sobrecarga)
                        capacidade_atual_de_energia += sobrecarga
                        sobrecarga = 0;

                    else:
                        gerador.gerar(capacidade_disponivel_no_gerador)
                        sobrecarga = sobrecarga - capacidade_disponivel_no_gerador
                        capacidade_atual_de_energia += capacidade_disponivel_no_gerador

                    if sobrecarga == 0 and geradores_analisados == quantidade_total_geradores:
                        print(  f"Sobrecarga estabilizada!")
        
    def relatorio_totais_e_custos(self):
        resultado = {}
        energia_total_por_tipo = {}
        custo_total_por_tipo = {}
        custo_medio_por_tipo = {}

        for gerador in self.geradores:
            if gerador.tipo_geracao not in energia_total_por_tipo:
                energia_total_por_tipo[gerador.tipo_geracao] = 0
            energia_total_por_tipo[gerador.tipo_geracao] += gerador.capacidade_atual

            if gerador.tipo_geracao not in custo_total_por_tipo:
                custo_total_por_tipo[gerador.tipo_geracao] = 0
            custo_total_por_tipo[gerador.tipo_geracao] += gerador.capacidade_atual * gerador.custo_mw

        for tipo_geracao, energia_total in energia_total_por_tipo.items():
            custo_total = custo_total_por_tipo.get(tipo_geracao, 0)
            custo_medio_por_tipo[tipo_geracao] = custo_total / energia_total if energia_total > 0 else 0

        energia_total_consumida = 0
        for carga in self.cargas:
            if carga.conectada:
                energia_total_consumida += carga.energia

        resultado["energia_total_por_tipo"] = energia_total_por_tipo
        resultado["custo_medio_por_tipo"] = custo_medio_por_tipo
        resultado["energia_total_consumida"] = energia_total_consumida

        print(resultado)
       

        
