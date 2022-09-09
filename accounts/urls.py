from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import SignupView, VerifyInviteView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('invite/<str:referral_code>/verify', VerifyInviteView.as_view(), name='user_invite'),
]
