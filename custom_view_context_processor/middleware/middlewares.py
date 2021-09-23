from middleware import views
from django.http import response
from django.shortcuts import redirect,HttpResponse
from django.urls.conf import path


def example_middleware(get_response):
    """Initialize code"""
    print("This is an example of middleware.")
    # inner function
    def inner_function(request):

        path = request.path
        print("Path is", path)
        if path in ["/mids/", "/mid/", "/mid"]:
            return redirect("index")

        response = get_response(request)
        print("This is after view")

        return response

    return inner_function


class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.session)
        path = request.path
        if path in ["/mids/", "/mid/", "/mid"]:
            return redirect("index")
        response = self.get_response(request)
        return response

    def process_exception(self, request, exeption):
        return HttpResponse(exeption)
    
    def process_view(self,request,view_func,view_args,view_kwargs):
        print("This is view process",view_func)
        return None
