from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Etudiant, Matiere, Classe, Notes
from django.db.models import Q
from django.template import loader
from django.shortcuts import render

# Create your views here.

def classes(request):

    classes = Classe.objects.all()
    context = {
    'classes': classes
    }
    if request.method == 'POST':
        nom = request.POST.get('nom')
        classe = Classe.objects.filter(nom=nom)
        if not classe.exists():
            classe = Classe(
                nom=nom
            )
            classe.save()
            context = {
                'insert':True,
                'classes': classes,
                'newClasse': classe,
                'message' : 'insertion effectue'
            }
        else:
            context = {
                'insert':True,
                'classes': classes,
                'newClasse': classe,
                'message':'insertion echoué'
            }
    if request.method == 'GET' and request.GET.get('_method')=='DELETE':
        context = {
        'insert':True,
        'classes': classes,
        'message':'Classe supprimer avec succes'
        }
        classe = get_object_or_404(Classe, pk=request.GET.get('_id'))
        classe.delete()



    return render(request,'FirstApp/classes.html',context)



def matieres(request):
    # request albums
    matieres = Matiere.objects.all()
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
    context = {
    'matieres': matieres
    }
    if request.method == 'POST':
        nom = request.POST.get('nom')
        coef = request.POST.get('coef')
        matiere = Matiere.objects.filter(nom=nom)
        if not matiere.exists():
            matiere = Matiere(
            nom=nom,
            coef=coef )
            matiere.save()
            context = {
            'matieres': matieres,
            'insert':True,
            'message':'Matiere inserer avec succes'
            }
        else:
            context = {
            'matieres': matieres,
            'insert':True,
            'message':'Matiere existe deja'
            }
    if request.method == 'GET' and request.GET.get('_method')=='DELETE':
        context = {
        'insert':True,
        'matieres': matieres,
        'message':'matiere supprimé'
        }
        matiere = get_object_or_404(Matiere, pk=request.GET.get('_id'))
        matiere.delete()
    return render(request,'FirstApp/matieres.html',context)

def listing(request, classe_id):
    classe = get_object_or_404(Classe,pk=classe_id)
    etudiants =Etudiant.objects.filter(classe_id=classe_id)
    context = {
    'classe':classe,
    'etudiants': etudiants
    }
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        classe_id= classe.id
        

        etudiant = Etudiant(
            nom=nom,
            prenom=prenom,
            classe=classe
        )
        etudiant.save()
        context = {
        'classe':classe,
        'etudiants': etudiants,
        'insert':True,
        'message':'Etudiant inserer avec succes'
        }
    if request.method == 'GET' and request.GET.get('_method')=='DELETE':
        context = {
        'classe':classe,
        'etudiants': etudiants,
        'insert':True,
        'message':'Etudiant supprimer avec succes'
        }
        etudiant = get_object_or_404(Etudiant, pk=request.GET.get('_id'))
        etudiant.delete()



    return render(request,'FirstApp/etudiants.html',context)





def search(request):
    pass

def search(request):
    query = request.GET.get('query')
    if not query:
        etudiants = Etudiant.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        etudiants = Etudiant.objects.filter(Q(nom__icontains=query)|Q(prenom__icontains=query))

    context = {
        'query' :query,
        'etudiants' :etudiants
    }
    return render(request,'FirstApp/search.html',context)

def releve(request,classe_id, etudiant_id):
    if request.method == 'POST':
        id = request.POST.get('_id')
        note = Notes.objects.get(pk=id)
        note.cc=request.POST.get('cc')
        note.ds=request.POST.get('ds')
        note.exam=request.POST.get('exam')
        note.save()
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    matieres = Matiere.objects.all()
    moyenne = 0
    coefs = 0
    nMatieres = 0
    for matiere in matieres:
        if etudiant.notes.filter(id=matiere.id).exists():
            print('exist')
        else:
            note = Notes(matiere=matiere,etudiant=etudiant,cc=0,ds=0,exam=0)
            note.save()

    notes=Etudiant.notes.through.objects.filter(etudiant_id=etudiant_id)
    for note in notes:
        moyenne = moyenne +(note.cc*0.2 + note.ds*0.3 + note.exam*0.5)*note.matiere.coef
        coefs=coefs+note.matiere.coef        
    moyenne = moyenne/(coefs)
    context = {
        'moyenne' : moyenne,
        'etudiant' : etudiant,
        'notes' :notes,
    }

    return render(request,'FirstApp/releve.html',context)