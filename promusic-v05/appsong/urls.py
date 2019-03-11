from django.urls import path
from .import views
from appsong.views import *
app_name = 'appsong'
urlpatterns=[
	path('princ/', views.gen_page_principale, name='page_princ'),
	path('chanson/<int:chanson_id>/', gen_page_chanson, name='page_chason'),
	

]
