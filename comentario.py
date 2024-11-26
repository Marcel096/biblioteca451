class Comentario:
    # relaciona os objetos Usuário e Livro na classe Comentário
    def __init__(self, usuario, livro, texto):  # Atributos
        self.usuario = usuario  # Referência ao objeto Usuario
        self.livro = livro  # Referência ao objeto Livro
        self.texto = texto

    """Criar os Métodos que se refere a class comentário"""
    def criar_comentario(self, usuario, livro, comentario):
        """O usuário faz um comentário."""
        pass

    def editar_comentario(self):
        """O usuário vai editar uma correção."""
        pass

    def remover_comentario(self):
        """O usuário vai remover o comentário."""
        pass