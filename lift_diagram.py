
class Painel:

    _gerenciadorElevador = None
    _elevador = None

    def __init__(self, gerenciadorElevador, elevador):
        self._elevador = elevador
        self._gerenciadorElevador = gerenciadorElevador

    def apertarBotaoNumero(self):
        #acao após usuario apertar numero do andar no painel
        pass

class Elevador:
    pass

class ElevadorEmManutencao(Elevador):

    _motivo = None
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def set_motivo(self, motivo):
        self._motivo = motivo


class ElevadorEmperrado(Elevador):

    _instance = None
    _motivo = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def tocarMusica(self):
        pass

    def chamarManutencao(self):
        pass


class ElevadorParado(Elevador):

    _instance = None
    _andar = None
    _motivo = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def abrirPorta(self):
        print("Abrindo Porta")

    def fecharPorta(self):
        print("Fechando Porta")

    def getAndarCorrente(self):
        return self._andar

    def setAndarCorrente(self, andar):
        self._andar = andar

class ElevadorEmMovimento(Elevador):

    def melhorCaminho(self):
        raise NotImplementedError

    def move(self):
        raise NotImplementedError

    def atualizaVelocidade(self):
        raise NotImplementedError

class ElevadorDescendo(ElevadorEmMovimento):

    _instance = None
    _velocidade = 0
    _andarCorrente = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def melhorCaminho(self):
        pass

    def move(self):
        #move para os andares escolhidos no painel
        pass

    def atualizaVelocidade(self):
        # aumenta/diminui a velocidade em caso de haver elevadores em manutencao
        pass

class ElevadorSubindo(ElevadorEmMovimento):

    _instance = None
    _velocidade = 0
    _andarCorrente = 0
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def melhorCaminho(self):
        pass

    def move(self):
        # move para os andares escolhidos no painel
        pass

    def atualizaVelocidade(self):
        #aumenta/diminui a velocidade em caso de haver elevadores em manutencao
        pass

class GerenciadorElevadores:

    _elevadoresList = None
    _emManutecaoCount = None
    _emperradoCount = None

    def __init__(self):
        self._elevadoresList = []
        self._emManutecaoCount = 0
        self._emperradoCount = 0

    def incrementaManutencaoCount(self):
        self._emManutecaoCount += 1
    def decrementaManutencaoCount(self):
        self._emManutecaoCount -= 1

    def getEmManutencaoCount(self):
        return self._emManutecaoCount

    def addElevadorToList(self, elevador):
        self._elevadoresList.append(elevador)

class ElevadoresEmManutencaoSubject:

    def notify(self):
        raise NotImplementedError

    def attach(self):
        raise NotImplementedError

    def detach(self):
        raise NotImplementedError


class ElevadoresEmManutencaoSubjectConcrete(ElevadoresEmManutencaoSubject):

    _elevadoresListToNotify = None
    _gerenciador = None

    def __init__(self, gerenciador):
        self._elevadoresListToNotify = []
        self._gerenciador = gerenciador
    def notify(self):
        #notifica os elevadores na lista _elevadoresListToNotify
        pass

    def attach(self, elevador):
        #adiciona elevadores na lista _elevadoresListToNotify
        pass

    def detach(self, elevador):
        #removem elevadores da lista
        pass

class ErrorElevadorEmperrado(Exception):
    pass

if __name__ == '__main__':
    print("Starting Lifts")
    gerenciador = GerenciadorElevadores()
    elevadorParado = ElevadorParado()
    elevadorParado.setAndarCorrente(0)
    gerenciador.addElevadorToList(elevadorParado)
    painel = Painel(gerenciador, elevadorParado)
    elevador_subject = ElevadoresEmManutencaoSubjectConcrete(gerenciador)

    while(True):
        #entrada do painel, sequencia de andares
        andares_selecionados = [2,4,8] #lista de andares digitados no painel

        for andar in andares_selecionados:
            andar_corrente = elevadorParado.getAndarCorrente()

            if andar_corrente < andar:
                #sobe elevador
                elevador_subindo = ElevadorSubindo()
                elevador_subject.attach(elevador_subindo)
                if gerenciador.getEmManutencaoCount() > 0:
                    elevador_subindo.atualizaVelocidade() #aumenta a velocidade de movimento
                try:
                    elevador_subindo.move()
                    elevador_parado = ElevadorParado()
                    elevador_parado.setAndarCorrente(andar)
                except ErrorElevadorEmperrado:
                    elevador_emperrado = ElevadorEmperrado()
                    elevador_emperrado.chamarManutencao()
                    elevador_emperrado.tocarMusica()
                    elevador_emmanutencao = ElevadorEmManutencao()
                    gerenciador.incrementaManutencaoCount()
            else:
                #desce elevador
                elevador_descendo = ElevadorDescendo()
                elevador_subject.attach(elevador_descendo)
                if gerenciador.getEmManutencaoCount() > 0:
                    elevador_descendo.atualizaVelocidade() #aumenta a velocidade de movimento
                try:
                    elevador_descendo.move()
                    elevador_parado = ElevadorParado()
                    elevador_parado.setAndarCorrente(andar)
                except ErrorElevadorEmperrado:
                    elevador_emperrado = ElevadorEmperrado()
                    elevador_emperrado.chamarManutencao()
                    elevador_emperrado.tocarMusica()
                    elevador_emmanutencao = ElevadorEmManutencao()
                    gerenciador.incrementaManutencaoCount()

