from django.urls import path
from . import views

urlpatterns = [
    # Routing to the landing page
    path('1',views.home),
    # Routing to the second page
    path('2',views.second),
    # Routing to the third page
    path('3',views.third),
]
