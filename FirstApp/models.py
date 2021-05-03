from django.db import models

# Create your models here.

ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


STUDENTS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]

class Classe(models.Model):
    nom = models.CharField(max_length=200, unique=True)
    def __str__(self):
      return self.nom


class Matiere(models.Model):
    nom = models.CharField(max_length=200, unique=True)  
    coef = models.IntegerField(blank=True, null=True)
    def __str__(self):
      return self.nom

class Etudiant(models.Model):
    nom = models.CharField(max_length=200)  
    prenom = models.CharField(max_length=200) 
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    notes = models.ManyToManyField(Matiere, through='Notes')
    def __str__(self):
      return self.nom+" "+self.prenom


class Notes(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE,related_name='+')
    cc = models.FloatField(blank=True, null=True)
    ds = models.FloatField(blank=True, null=True)
    exam = models.FloatField(blank=True, null=True)
    class Meta:
      unique_together = (("matiere", "etudiant"),)
    def __str__(self):
      return ""+str(self.cc)+" "+str(self.ds)+" "+str(self.exam)+" "+str(self.etudiant)+" "+str(self.matiere)
 