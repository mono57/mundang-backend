from django.urls import path

from accounts.views import SignupView, VerifyInviteView, DashboardTemplateView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('invite/<str:referral_code>/verify', VerifyInviteView.as_view(), name='user_invite'),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
]
