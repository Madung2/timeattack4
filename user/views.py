
from django.shortcuts import render, redirect
from .models import UserClass
import hashlib
from django.http import HttpResponse


# Create your views here.
def sign_up_view(request):
    if request.method =='GET':
        return render(request, 'index.html')
        #'user/signup.html'
    elif request.method == 'POST':
        email = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if len(password) < 8:
            return redirect('/index')
        elif '@' not in email:
            return redirect('/index')
        else:
            pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

            new_user = UserClass()
            new_user.email = email
            new_user.password = pw_hash
            new_user.save()
            return HttpResponse('회원가입 완료')


        return render(request, '')

