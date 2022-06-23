from django.urls import path

from accounts.views import SignupView, VerifyInviteView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('invite/<str:referral_code>/verify', VerifyInviteView.as_view()),
]
