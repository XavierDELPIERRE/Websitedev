from django.shortcuts import render
import os

from django.templatetags.static import static

# Calculate django application execute directory path.
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
from django.http import HttpResponse
from django.urls import reverse
from jinja2 import Environment
from django.template.loader import render_to_string

# import id

with open(
    os.path.normcase(PROJECT_PATH + """/donnees/ml.txt"""), mode="r", encoding="utf-8"
) as f:
    mllines = r"{}".format(f.read())
dictpages = {
    "homepage": "home",
    "pressite": "pressite",
    "presperso": "presperso",
    "projets": "projets",
    "rss": "rss",
    "afaire": "afaire",
    "ml": "ml",
}
dictpages2 = {
    "Athome": "Home",
    "Accueil": "Athome",
    "About": "About",
    "Contact": "Contact",
    "Mesprojets": "Mes-projets",
    "Lesite": "Le-site",
    "betaml": "Mentions-légales",
}
index_file_path = os.path.normcase(PROJECT_PATH + """/templ/templweb.html""")
index2_file_path = os.path.normcase(PROJECT_PATH + """/templ/niceview.html""")


def home(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/donnees/acc.txt"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())

    text = {"texte": acc}
    return render(request, index_file_path, {**text, **dictpages})


def Athome(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/Site1/Accueil.html"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())
    text = {"titre": "Home","texte": acc}
    return render(request, index2_file_path, {**text, **dictpages2})


def About(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/Site1/About.html"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())

    text = {"titre": "About","texte": acc}
    return render(request, index2_file_path, {**text, **dictpages2})


def Contact(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/Site1/Contact.html"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())
    text = {"titre": "Contact","texte": acc}
    return render(request, index2_file_path, {**text, **dictpages2})


def Mesprojets(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/Site1/Mes-projets.html"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())
    text = {"titre": "Mes-projets","texte": acc}
    return render(request, index2_file_path, {**text, **dictpages2})


def Lesite(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/Site1/Le-site.html"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())
    text = {"titre": "Le-site","texte": acc}
    return render(request, index2_file_path, {**text, **dictpages2})

def betaml(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/Site1/Mentions-légales.html"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())
    text = {"titre": "Mentions-légales","texte": acc}
    return render(request, index2_file_path, {**text, **dictpages2})


def projets(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/donnees/projets.txt"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())

    text = {"texte": acc}
    return render(request, index_file_path, {**text, **dictpages})


def pressite(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/donnees/pressite.txt"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())

    text = {"texte": acc}
    return render(request, index_file_path, {**text, **dictpages})


def presperso(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/donnees/profile.txt"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        profile = r"{}".format(f.read())

    text = {"texte": profile}

    return render(request, index_file_path, {**text, **dictpages})


def rss(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/donnees/news.csv"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())

    text = {"texte": acc}
    return render(request, index_file_path, {**text, **dictpages})


def afaire(request):
    with open(
        os.path.normcase(PROJECT_PATH + """/donnees/taches.csv"""),
        mode="r",
        encoding="utf-8",
    ) as f:
        acc = r"{}".format(f.read())

    text = {"texte": acc}
    return render(request, index_file_path, {**text, **dictpages})


def ml(request):
    text = {"texte": mllines}
    return render(request, index_file_path, {**text, **dictpages})
