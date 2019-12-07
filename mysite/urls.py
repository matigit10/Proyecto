from django.contrib import admin
from django.urls import path, include
from catalog import views as catalog_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns =[
	path ('admin/', admin.site.urls),
	path ('',catalog_views.inicio, name='inicio'),
	path ('drivers/',catalog_views.driverx, name='drivers'),
	path ('enlaces/',catalog_views.link, name='links'),
	path('login/', TemplateView.as_view(template_name='registration/login.html'), name='log'),
	path ('registrar/',catalog_views.ingresar, name='registro'),
	path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
	path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

	]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)