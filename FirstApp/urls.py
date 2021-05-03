from django.conf.urls import url
from django.urls import include, path


from . import views # import views so we can use them in urls.

urlpatterns = [
    url(r'^$', views.classes,name='classes'),
    url(r'^(?P<classe_id>[0-9]+)/$', views.listing,name='listing'),
    url(r'^(?P<classe_id>[0-9]+)/(?P<etudiant_id>[0-9]+)$', views.releve,name='releve'),
    url(r'^search/$', views.search,name='search'),
    url(r'^matiere/$', views.matieres,name='matiere'),
]