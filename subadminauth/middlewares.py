from django.shortcuts import render, redirect
def checksubadminfunction(get_response):
    def subadmin_function(request):
        if not request.session.get('subadmin_id'):
            return redirect("authentication")
        else:
            response = get_response(request)
            return response
    return subadmin_function

