
from django.http import HttpResponse


def home(request ):
    return HttpResponse("Bem-vindo à Loja Geek!")


def sobre(request):
    return HttpResponse(
        "A Loja Geek vende camisetas, canecas, colecionáveis e acessórios para fãs de cultura pop."
    )

