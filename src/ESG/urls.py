from django.urls import path
from .views import BoundaryView, StatementView, SourceView, GetPNView
urlpatterns = [
    path('boundary/create/', BoundaryView.as_view(), name="boundary_create"),
    path('boundary/retrieve/', BoundaryView.as_view(), name="boundary_retrieve"),
    path('boundary/revise/', BoundaryView.as_view(), name="boundary_revise"),
    path('boundary/delete/', BoundaryView.as_view(), name="boundary_delete"),
    path('statement', StatementView.as_view(), name="statement"),
    path('source', SourceView.as_view(), name='source'),
    path('PN/get', GetPNView.as_view(), name='get_pn')
]
