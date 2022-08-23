from django.urls import path
from .import views
urlpatterns = [
    path('actor', views.ActorDetailView.as_view(), name="ActorDetailView"),
    path('actor/<int:pk>', views.ActorUpdateView.as_view(), name="actor-detail"),
    path('details', views.DetailsInfoView.as_view(), name="DetailsInfoView"),
    path('details/<int:pk>', views.DetailsUpdateView.as_view(), name="details-detail"),
]