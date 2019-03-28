from django.urls import path
from .import views
from appsong.views import *

app_name='appsong'
urlpatterns = [
    path('princ/', views.gen_page_principale, name='page_princ'),
    path('chanson/<int:chanson_id>/', views.gen_page_chanson, name='chanson_id'),
	path('chanson/nouv/', views.gen_nouv_chanson, name='nouv_chanson'),
    path('chanson/<int:chanson_id>/modif/',views.gen_modif_chanson,name='modif_chanson')
]
