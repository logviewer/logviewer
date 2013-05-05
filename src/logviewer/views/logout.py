from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_action(request):
    '''
        Logout action for user

        @param request HTTP request object
        @returns HTTP redirect to login page
    '''
    logout(request)
    return redirect('/login')
