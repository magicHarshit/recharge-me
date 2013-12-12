from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect

from transactions.models import PhoneNumber, UserAccount
from operators.views import which_operator

import random

@login_required(login_url='/login/')
def home(request):
    message = ''
    if request.method == 'POST':
        phone_numbers = request.POST.get('phnumbers')
        is_everything_ok = check_input(phone_numbers)
        if is_everything_ok:
            ph_numb_objects = []
            for numb in phone_numbers.split(','):
                ph_numb_objects.append(
                    PhoneNumber(
                        phnumber=numb,
                        added_by=request.user,
                        operator=which_operator()))
            PhoneNumber.objects.bulk_create(ph_numb_objects)
            if not request.user.useraccount:
                UserAccount.objects.create(account=request.user)
            return HttpResponseRedirect('/profile/mynumbers/')
        message = 'Please enter correct phone numbers only'
    return render_to_response('home.html',{'message':message},
                context_instance=RequestContext(request))

def check_input(phone_numbers):
    if phone_numbers:
        ph_numbers_list = phone_numbers.split(',')
        for ph_number in ph_numbers_list:
            if not ph_number.isdigit() or len(ph_number)!=10:
                return
        return True

def rechareresponse():
    return random.sample([True,False],1)