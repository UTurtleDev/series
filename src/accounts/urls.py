from django.urls import path, include

from accounts.views import login_user
from suivi.views import index

urlpatterns = [
    path('', login_user, name='login'),

]