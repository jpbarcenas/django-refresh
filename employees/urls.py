from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add', views.employee_add, name='employee_add'),
    path('<int:pk>/', views.employee_details, name='employee_details'),
    path('<int:pk>/edit', views.employee_edit, name='employee_edit'),
    # path('employees', include('employees.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)