from django.urls import path, include
from rest_framework.authtoken import views
from .views import home_view


urlpatterns = [
    path('', home_view, name='api.home'),
    path('category/', include('api.category.urls'))
]
