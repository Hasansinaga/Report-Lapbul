from django.urls import path
from . import views

app_name = 'lapbul_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('lapbul/', views.lapbul, name='lapbul'),
    path('lapbul/form_0000/', views.form_0000, name='form_0000'),
    path('lapbul/form_0001/', views.form_0001, name='form_0001'),
    path('lapbul/form_0002/', views.form_0002, name='form_0002'),
    path('lapbul/form_0003/', views.form_0003, name='form_0003'),
    path('lapbul/form_0004/', views.form_0004, name='form_0004'),
    path('lapbul/form_0005/', views.form_0005, name='form_0005'),
    path('lapbul/form_0006/', views.form_0006, name='form_0006'),
    path('lapbul/form_0007/', views.form_0007, name='form_0007'),
    path('lapbul/form_0008/', views.form_0008, name='form_0008'),
    path('lapbul/form_0009/', views.form_0009, name='form_0009'),
    path('lapbul/form_0010/', views.form_0010, name='form_0010'),
    path('lapbul/form_0011/', views.form_0011, name='form_0011'),
    path('lapbul/form_0012/', views.form_0012, name='form_0012'),
    path('lapbul/form_1100/', views.form_1100, name='form_1100'),
    path('lapbul/form_1200/', views.form_1200, name='form_1200'),
    path('lapbul/form_1300/', views.form_1300, name='form_1300'),
    path('lapbul/form_1400/', views.form_1400, name='form_1400'),
    path('lapbul/form_1401/', views.form_1401, name='form_1401'),
]
