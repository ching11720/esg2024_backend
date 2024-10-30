from django.urls import path
from .views import BoundaryView# , SourceView
urlpatterns = [
    path('boundary', BoundaryView.as_view(), name="boundary"),
    # path('source', SourceView.as_view(), name="source"),
]
