class Pessoa:
        def __init__(self):#metodo construtor
            self.nome = ""
            self.telefone = ""
            self.endereco = ""

        #metodos de acesso (gets & sets)
        def getNome(self):
            return self.nome

        def getTelefone(self):
            return self.telefone

        def getEndereco(self):
            return self.endereco

        def setNome(self, nome):
            self.nome = nome

        def setTelefone(self, telefone):
            self.telefone = telefone

        def setEndereco(self, endereco):
            self.endereco = endereco

        #metodo cadastrar:
        def cadastrar(self, nome, telefone, endereco):
            self.setNome(nome)
            self.setTelefone(telefone)
            self.setEndereco(endereco)

        #metodo consultar pessoa
        def consultarTudo(self):
            return "Nome: {}\nTelefone: {}\nEndereço: {}".format(self.getNome(), self.getTelefone(), self.getEndereco())
