from django.shortcuts import render

def login(request):
    return render(request, 'diary/diary_template.html')
