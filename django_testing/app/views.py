from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.db_queries import book_list, book_list_select_related, store_list, store_list_prefetch_related
# from app.tasks import my_first_task
# Create your views here.
@api_view(["GET"])
def Book_list(request):
    print("Without select: ")
    book_list()
    print("With select_related: ")
    book_list_select_related()
    print("Without prefetch related: ")
    store_list()
    print("With prefetch related: ")
    store_list_prefetch_related()
    

    return Response({"status":"ok"})

@api_view(["GET"])
def index(request):
    # my_first_task.delay(20)
    
    return Response({"status":"ok"})
