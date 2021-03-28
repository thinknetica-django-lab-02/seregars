from django.shortcuts import render


def index(request):
    turn_on_block = True
    user = request.user
    return render(request, 'main/index.html', {'turn_on': turn_on_block, 'user': user})

