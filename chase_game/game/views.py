from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'game/index.html')

def game_view(request):
    return render(request, 'game/game_interface.html')