from django.urls import path
from .views import AndelansListView
# andelans app url patterns

urlpatterns = [
    path('api/andelans/', AndelansListView.as_view()),
]
