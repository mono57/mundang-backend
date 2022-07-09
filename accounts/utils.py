
from allauth.account.adapter import get_adapter

def perform_login(request, user):
    adapter = get_adapter()
    adapter.login(request, user)