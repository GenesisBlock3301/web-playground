from django.shortcuts import render
# from django.forms
from .models import *
from django.http import JsonResponse


def home(request):
    stud = User.objects.all()
    return render(request, 'home/home.html', {'stud': stud})


def save_data(request):
    if request.method == "POST":
        sid = request.POST.get('stuid', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if name and email and password:
            if sid == '':
                user = User(name=name, email=email, password=password)
            else:
                user = User(id=sid,name=name, email=email, password=password)
            user.save()
            # stud = User.objects.all()
            """
            output
            <QuerySet [<User: Nur Amin Sifat>, <User: Jamy>,
             <User: Nur>, <User: Nas>, <User: Sumon>, <User: Supin>,
              <User: Footwear>]>
            """
            stud = User.objects.values()
            """
            output
            <QuerySet [
              {'id': 1, 'name': 'Nur Amin Sifat', 'email': 'nur15-1463@diu.edu.bd', 'password': 'nas12345'},
              {'id': 2, 'name': 'Jamy', 'email': 'jamy@gmail.com', 'password': 'w.WhAqfE55tB9ds'},
              {'id': 3, 'name': 'Nur', 'email': 'nur15-1463@diu.edu.bd', 'password': 'nur'},
              {'id': 4, 'name': 'Nas', 'email': 'nas@gmail.com', 'password': 'nas'}, 
              {'id': 5, 'name': 'Sumon', 'email': 'sumon@gmail.com', 'password': 'sumon'},
              {'id': 6, 'name': 'Supin', 'email': 'sifat@gmail.com', 'password': 'fsfa'}
              ]>
            """
            student_data = list(stud)
            return JsonResponse({'status': "Save","student_data":student_data})
        else:
            return JsonResponse({'status': 0})


# Delete data
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid','')
        print(id)
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


# edit data
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid','')
        print(id)
        student = User.objects.get(pk=id)
        student_data = {
            "id":student.id,
            'name':student.name,
            'email':student.email,
            'password':student.password,
        }
        return JsonResponse(student_data)



