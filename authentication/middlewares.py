from django.shortcuts import render, redirect
def checkuserauthfunction(get_response):
    def user_function(request):
        if not request.session.get('user_id'):
            return redirect("authentication")
        else:
            response = get_response(request)
            return response
    return user_function

