from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, mundo! Você está na view 'index' do app polls.")
