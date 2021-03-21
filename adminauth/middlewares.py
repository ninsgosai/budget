from django.shortcuts import render, redirect
def checkadminauth(get_response):
    def admin_function(request):
        if not request.session.get('admin_id'):
            return redirect("authentication")
        else:
            response = get_response(request)
            return response
    return admin_function

