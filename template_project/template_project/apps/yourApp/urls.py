"""from django.urls import path

from . import views

#To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.
app_name = 'yourApp'

urlpatterns = [
    # ex: /yourApp/
    path('', views.index, name='index'),
    # ex: /yourApp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /yourApp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /yourApp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]"""

from django.urls import path

from . import views

app_name = 'yourApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]