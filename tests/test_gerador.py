from Classes.gerador import Gerador
from Classes.carga import Carga
from Classes.sistema_de_geracao import SistemaDeGeracao


from Classes.carga import Carga
from Classes.gerador_qualificado import GeradorQualificado
from Classes.sistema_de_geracao_verde import SistemaDeGeracaoVerde

def test_exercicio1():

    print()

    ps = SistemaDeGeracao()
    #Geradores
    g1 = Gerador("G1", 100)
    g2 = Gerador("G2", 150)

    #Cargas
    c1 = Carga("C1", 50)
    c2 = Carga("C2", 110)
    c3 = Carga("C3", 80)
    
    ps.adicionar_gerador(g1)
    ps.adicionar_gerador(g2)

    ps.adicionar_carga(c1)
    ps.adicionar_carga(c2)
    ps.adicionar_carga(c3)

    #Conecta as Cargas
    c1.conectar()
    c2.conectar()
    c3.conectar()
    c3.conectar()

    ps.balancear()

    print(f"{g1.nome}: {g1.capacidade_atual} MW")
    print(f"{g2.nome}: {g2.capacidade_atual} MW")
    
    return


def test_exercicio2():

    print()

    ps_verde = SistemaDeGeracaoVerde()
    #Geradores
    g1 = GeradorQualificado("G1", 100, "eólica", 5)
    g2 = GeradorQualificado("G2", 150, "solar", 6)
    g3 = GeradorQualificado("G3", 90, "hidrelétrica", 4)
    g4 = GeradorQualificado("G4", 120, "termelétrica", 8 )
    g5 = GeradorQualificado("G5", 200, "hidrelétrica", 9 )
    g6 = GeradorQualificado("G6", 40, "termelétrica", 3 )
    g7 = GeradorQualificado("G7", 40, "solar", 1 )

    #Cargas
    c1 = Carga("C1", 50)
    c2 = Carga("C2", 110)
    c3 = Carga("C3", 80)
    c4 = Carga("C4", 120)
    c5 = Carga("C5", 200)
    c6 = Carga("C6", 140)
    c7 = Carga("C7", 40)
    c8 = Carga("C8", 90)
    
    ps_verde.adicionar_carga(c1)
    ps_verde.adicionar_carga(c2)
    ps_verde.adicionar_carga(c3)
    ps_verde.adicionar_carga(c4)
    ps_verde.adicionar_carga(c5)
    ps_verde.adicionar_carga(c6)

    # Primeiro Adicionar os geradores termelétrica para testar função de ordenação deixando eles sempre em último independente do custo
    ps_verde.adicionar_gerador(g4)
    ps_verde.adicionar_gerador(g6)
    ps_verde.adicionar_gerador(g1)
    ps_verde.adicionar_gerador(g2)
    ps_verde.adicionar_gerador(g3)
    ps_verde.adicionar_gerador(g5)

    # Essa carga irá gerar uma sobrecarga onde os geradores já estão em potencia máxima oq ira desativar as cargas em ordem de consumo
    ps_verde.adicionar_carga(c7)

    # Ao adicionar gerador novo ira estabilizar
    ps_verde.adicionar_gerador(g7)

    print(f"{g1.nome}: {g1.capacidade_atual} MW: tipo de energio {g1.tipo_geracao}")
    print(f"{g2.nome}: {g2.capacidade_atual} MW: tipo de energio {g2.tipo_geracao}")
    print(f"{g3.nome}: {g3.capacidade_atual} MW: tipo de energio {g3.tipo_geracao}")
    print(f"{g4.nome}: {g4.capacidade_atual} MW: tipo de energio {g4.tipo_geracao}")
    print(f"{g5.nome}: {g5.capacidade_atual} MW: tipo de energio {g5.tipo_geracao}")
    print(f"{g6.nome}: {g6.capacidade_atual} MW: tipo de energio {g6.tipo_geracao}")
    print(f"{g7.nome}: {g7.capacidade_atual} MW: tipo de energio {g7.tipo_geracao}")

    
    # Adicionando essa carga irá desconectar novamente as excedentes para testar função de listagem de cargas desconectadas
    # Irá desconectar cargas c1 e c7 totalizando os 90 de energia excedentes
    ps_verde.adicionar_carga(c8)
    ps_verde.listar_cargas_desconectadas()

    # Exibindo Relátorio
    ps_verde.relatorio_totais_e_custos()