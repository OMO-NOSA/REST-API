from django.urls import path
from update.views import update_model_detail_view

urlpatterns = [
    path('', update_model_detail_view)
]
