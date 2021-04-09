from django.shortcuts import render,HttpResponse,redirect


def cookie_session(request):
    #set test cookie when a browser request a page
    request.session.set_test_cookie()
    return HttpResponse("<h1>Data Flair</h1>")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        #this method delete the test cookie
        request.session.delete_test_cookie()
        response = HttpResponse("Data<br> cookie created")
    else:
        response = HttpResponse("Your browser dont accept cookie")
    return response


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'admin12345'
    return HttpResponse("<h1>Session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to my session experiment</h1><br>"
    if request.session.get('name'):
       response += f"Name is: {request.session.get('name')}"
    if request.session.get('password'):
        response += f"Name is: {request.session.get('password')}"
        return HttpResponse(response)
    else:
        redirect('create_session')
