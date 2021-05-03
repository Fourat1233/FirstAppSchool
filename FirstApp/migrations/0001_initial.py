# Generated by Django 3.2 on 2021-04-26 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
                ('prenom', models.CharField(max_length=200, unique=True)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
                ('coef', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc', models.FloatField(blank=True, null=True)),
                ('ds', models.FloatField(blank=True, null=True)),
                ('exam', models.FloatField(blank=True, null=True)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='FirstApp.etudiant')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='notes',
            field=models.ManyToManyField(through='FirstApp.Notes', to='FirstApp.Matiere'),
        ),
    ]
