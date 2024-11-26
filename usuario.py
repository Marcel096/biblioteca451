class Usuario:
    def __init__(self, nome, email, endereco, telefone):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    def cadastrar(self):
        '''Exibe os dados do usuário cadastrado.'''
        print('Nome: {}'.format(self.nome))
        print('Email: {}'.format(self.email))
        print('Endereço: {}'.format(self.endereco))
        print('Telefone: {}'.format(self.telefone))

    def deletar(self):
        '''Deletar a conta do usuário.'''
        print('Conta do usuário {} foi deletada'.format(self.nome))
        self.nome = None
        self.email = None
        self.endereco = None
        self.telefone = None
    
    