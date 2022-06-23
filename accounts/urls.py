from django.urls import path
from accounts.views import SignupView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]
