from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # フォーム処理を追加（例：メール送信）
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
