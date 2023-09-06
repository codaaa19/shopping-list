from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Tsabit Coda Rafisukmawan',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
