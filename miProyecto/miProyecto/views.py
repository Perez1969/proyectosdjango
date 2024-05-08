from django.http import HttpResponse


def saludo(request,usuario):
    return HttpResponse(f"""<b>Hola {usuario}</b> <img src="https://es.wikipedia.org/static/images/icons/wikipedia.png" alt="Teclado" />""")
