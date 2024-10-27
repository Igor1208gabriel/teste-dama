from django.db import models


class Livro(models.Model):
    id = models.BigAutoField(editable=False, unique=True, primary_key=True)
    titulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    editora = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    descricao = models.TextField()
    dataPublicacao = models.DateField()

    def __str__(self):
        return f"{self.autor}, {self.titulo}"


class Usuario(models.Model):
    id = models.BigAutoField(editable=False, unique=True, primary_key=True)
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=30)
    senha = models.CharField(max_length=128)
    livrosFavoritos = models.ManyToManyField(Livro, related_name="usuarios_favoritos")
    
class Mensagem(models.Model):
    id = models.BigAutoField(editable=False, unique=True, primary_key=True)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    de = models.ForeignKey(Usuario, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    para = models.ForeignKey(Usuario, related_name='mensagens_recebidas', on_delete=models.CASCADE)

    def __str__(self):
        return f"Mensagem de {self.de} para {self.para}"