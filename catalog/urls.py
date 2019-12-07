from django.urls import path 
from .import views

urlpatterns=[
	path('',views.index,name='index')
	path('TarjetasVideo/', views.TarjetasVideos.as_view(), name='tarjetas'),
	path ('registro/', registro, name='registrar')
	path('signup/', views.SignUp.as_view(), name='signup'),
]

urlpatterns += [
    path('driver/create/', views.AgregarDriver.as_view(), name='Nuevo Driver'),
    path('driver/<int:pk>/update/', views.DriverUpdate.as_view(), name='Actualizar Driver'),
    path('driver/<int:pk>/delete/', views.DeleteDriver.as_view(), name='Eliminar Driver'),
]
