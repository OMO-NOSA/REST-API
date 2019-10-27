from django.urls import path
from status.views import StatusListSearchAPIView

urlpatterns = [
    path('StatusApi', StatusListSearchAPIView.as_view()),
]
