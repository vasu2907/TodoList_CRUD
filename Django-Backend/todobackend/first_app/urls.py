from django.urls import re_path
from first_app import views
from django.conf import *
from django.views.decorators.csrf import csrf_exempt
import re
app_name = 'first_app'

urlpatterns = [
        re_path(r'^todo/[0-9]*$',csrf_exempt(views.Todos.as_view())),
]