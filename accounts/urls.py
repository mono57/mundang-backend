from django.urls import path

from accounts.views import SignupView, VerifyInviteView, DashboardTemplateView

app_name = 'accounts'

urlpatterns = [
    path('register/', SignupView.as_view(), name='signup'),
    path('invite/<str:referral_code>/verify', VerifyInviteView.as_view(), name='user_invite'),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
]
