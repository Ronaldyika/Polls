from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    #path('results/<int:poll_id>', views.results, name='results'),
    path('result',views.result,name='result'),
    #path('vote/<int:poll_id>/',views.vote, name='vote'),
    path('votes',views.vote,name='votes'),
    path('createnow>',views.createnow,name='createnow')
]
