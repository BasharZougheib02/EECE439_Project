from django.urls import include, path
from .views import home, success, view, edit, delete, error
urlpatterns = [
 path('success/', success, name='success'),
 path('', home, name='home'),
 path('contact/<id>', view, name='view'),
 path('edit/<id>', edit, name='edit'),
 path('delete/<id>', delete, name='delete'),
 path('error/', error, name='error')
]
