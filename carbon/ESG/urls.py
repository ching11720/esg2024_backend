from django.urls import path
from .views import BoundaryView
from pm import views
urlpatterns = [
    path('boundary', BoundaryView.as_view(), name="boundary"),
    # path('source/', views.source_create, name="source_create"),
    # path('source/<str:SRID>/', views.source_retrieve, name="source_retrieve"),
]
