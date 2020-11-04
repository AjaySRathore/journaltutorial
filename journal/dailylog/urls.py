from django.urls import path
from dailylog.views import gratitude_view

urlpatterns =[
    path('gratitude/<int:pk>', gratitude_view),

]