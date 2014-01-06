import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import UserAccount


def home(request):
    posts = []
    return render_to_response('index.html', {'posts': posts}, context_instance=RequestContext(request))


def update_balance(request):
    post_data = json.loads(request.raw_post_data)
    if post_data and request.user.is_authenticated():
        balance = int(post_data.get('balance'))
        user_account = UserAccount.objects.get(account=request.user)
        old_balance = user_account.balance
        if post_data.get('action') == 'Recharge':
            total_balance = old_balance - balance
        else:
            total_balance = balance+old_balance
        user_account.balance = total_balance
        user_account.save()
        data = {'balance': user_account.balance}
        return HttpResponse(json.dumps(data), content_type="application/json")
