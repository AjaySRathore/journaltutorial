# Journal App

This app is a empty Django project based repository. It contains one app named **dailylog**. This app lets a user add daily logs. Logs are of three types:  Gratitude, Conclusion, Goal.

User is able to see history of activities in weekly and monthly groups.
For more details follow the [Use Case](https://lucid.app/invitations/accept/ebb5cec7-22d2-4bb0-8352-269905de93b6)

## Installation Instructions.
These are the instructions for Linux OS. All commands are ran in linux shell.
1. Clone the directory using `git clone <repo link>`
2. Create virtualenv using `python3.8 -m venv <name of your env>`
3. Activate virtualenv using `source <name of your env>/bin/activate`
4. Go to Directory journal/journal. This is the project settings directory. It should have a file name settings.py. Here create a new file named local_settings.py
5. add one line in this file declaring a variable `SECRET_KEY = <50 char long random string with number, string literals, special characters>`. example `SECRET_KEY = "_bjg^rwo+ez^t%cx+mj6b#ms-v7#edru$#l96cxk($58xt7i*-"`
6. Go one directory up with `cd ..` and migrate the models to your local database `./manage.py migrate`
7. If no error on step 6 then run the local server with `./manage.py runserver`
8. Go to http://127.0.0.1:8000/ or another link if specified in the terminal screen.


## Instructions for making models.
These are the instructions for Linux OS.
1. Open directory **journal/dailylog**. Find the file models.py.
2. Write all related database related schema here using django ORM.

Example of a models:
```from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
Read more information on [Django Fields References](https://docs.djangoproject.com/en/3.1/ref/models/fields/)

## Instructions for adding a view.
There are the instructions for Linux OS.
1. Open directory **journal/dailylog**. Find the file views.py.
2. All the views that connect django templates with django Models should be added here.
3. Map the views to specific urls by editing urls.py.
4. Add dailylog urls to journal/urls.py using `include()` method.

Example of views:
```from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```
Learn more about [writing views](https://docs.djangoproject.com/en/3.1/topics/http/views/)

## Instructions for adding a template and static files.
1. Open directory **journal/dailylog/templates/dailylog**.
2. Add all html templates here.
3. Open directory **journal/dailylog/static/dailylog/styles**.
4. add all the css here.

Example of templates:
```<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

Learn more about [Django Templates](https://docs.djangoproject.com/en/3.1/ref/templates/language/#templates)
