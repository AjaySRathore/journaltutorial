from django.shortcuts import render
from dailylog.models import Gratitude

def gratitude_view(request, pk):
    gratitude = Gratitude.objects.get(id=pk)
    context = {
        "gratitude_value" : gratitude.gratitude,
        "today_date" : gratitude.day_id.day
    }
    template_name = "dailylog/gratitude.html"
    return render(request, template_name, context)
