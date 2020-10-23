from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Acu, Insurance
from .forms import AcuForm
from .forms import InsuranceForm
import requests
from bs4 import BeautifulSoup

# Create your views here.


def index(request):
    clinics = Acu.objects.all()
    return render(request, 'Acu_Insurance/index.html', {'clinics': clinics})


def home(request):
    return render(request, 'Acu_Insurance/Acu_Insurance_home.html')


def thanks(request):
    return render(request, 'Acu_Insurance/Acu_Insurance_Thanks.html')


def add(request):
    form = AcuForm(request.POST or None)
    if request.method == 'POST':
        form = AcuForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, }
    return render(request, 'Acu_Insurance/Acu_Insurance_add.html', context)


def addInsurance(request):
    if request.method == 'POST':
        forms = InsuranceForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Thanks')
    else:
        forms = InsuranceForm()
    return render(request, 'Acu_Insurance/Acu_Insurance_addInsurance.html', {'forms': forms})


def details(request, pk):
    clinic = get_object_or_404(Acu, pk=pk)
    context = {'clinic': clinic}
    return render(request, 'Acu_Insurance/Acu_Insurance_details.html', context)

def edit(request, pk):
    clinic = get_object_or_404(Acu, pk=pk)
    if request.method == "POST":
        form = AcuForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('details', pk=clinic.pk)
    else:
        form = AcuForm(instance=clinic)
    return render(request, 'Acu_Insurance/Acu_Insurance_edit.html', {'form': form})


def delete(request, pk):
    clinic = get_object_or_404(Acu, pk=pk)
    if request.method == 'POST':
        clinic.delete()
        return redirect('index')
    context = {'clinic': clinic}
    return render(request, 'Acu_Insurance/Acu_Insurance_delete.html', context)


def latest(request):
    page = requests.get("https://news.harvard.edu/gazette/story/2020/08/study-reveals-acupuncture-affects-disease-course/")
    soup = BeautifulSoup(page.content, 'html.parser')
    # match = soup.title.text
    # print(match)
    # match = soup.div
    # print(match)
    # match = soup.find('div')
    # print(match)
    article = soup.find('div', class_='article-body basic-text do-drop-cap')
    # print(article)

    # text = article.p
    # print(text)
for p in soup.find_all('p', class_='article-body basic-text do-drop-cap'):

















