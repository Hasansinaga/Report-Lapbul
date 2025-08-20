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

    # Start of Changes made by William 

    path('lapbul/form_0013/', views.form_0013, name='form_0013'),
    path('lapbul/form_0015/', views.form_0015, name='form_0015'),
    path('lapbul/form_0016/', views.form_0016, name='form_0016'),
    path('lapbul/form_0017/', views.form_0017, name='form_0017'),
    path('lapbul/form_0018/', views.form_0018, name='form_0018'),
    path('lapbul/form_0019/', views.form_0019, name='form_0019'),
    path('lapbul/form_0020/', views.form_0020, name='form_0020'),
    path('lapbul/form_0021/', views.form_0021, name='form_0021'),
    path('lapbul/form_0100/', views.form_0100, name='form_0100'),
    path('lapbul/form_0101/', views.form_0101, name='form_0101'),
    path('lapbul/form_0200/', views.form_0200, name='form_0200'),
    path('lapbul/form_0300/', views.form_0300, name='form_0300'),
    path('lapbul/form_0400/', views.form_0400, name='form_0400'),

    # End of changes made by William
]
