from Classes.gerador import Gerador

class GeradorQualificado(Gerador):

    def __init__(self, nome, capacidade_maxima, tipo_geracao, custo_mw):
            super().__init__(nome,capacidade_maxima)
            self.capacidade_atual = 0
            self.tipo_geracao = tipo_geracao
            self.custo_mw = custo_mw
    
    def exportar_dados(self):
        return {
            'Nome': self.nome,
            'Custo por MW': self.custo_mw,
            'Tipo de Geração': self.tipo_geracao,
            'Capacidade Atual (MW)': self.capacidade_atual,
            'Capacidade Máxima (MW)': self.capacidade_maxima,
        }