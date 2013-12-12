from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from transactions.models import PhoneNumber

def signup(request):
    signupform = UserCreationForm(request.POST or None)
    if signupform.is_valid():
        signupform.save()
        return HttpResponseRedirect('/')
    return render_to_response('login.html', {'form': signupform},
        context_instance=RequestContext(request))

@login_required(login_url='/login/')
def showmynumbers(request):
    all_numbers = PhoneNumber.objects.filter(added_by=request.user)
    return render_to_response('mynumbers.html', {'trans': all_numbers} ,
        context_instance=RequestContext(request))

def profile(request):
    return showmynumbers(request)

def addmoney(request):
    if request.method == 'POST':
        balance = request.POST.get('balance')
        if balance and balance.isdigit():
            request.user.useraccount.balance+= abs(int(balance))
            request.user.useraccount.save()
    return render_to_response('addaccount.html',
        {'current_balance':request.user.useraccount.balance},
        context_instance=RequestContext(request))        