from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from transactions.models import PhoneNumber
from rechargeproviders.models import RechargeApi
from rechargeproviders.views import rechareresponse

def recharge(request, ph_id):
    ph_numb = get_object_or_404(PhoneNumber, pk=int(ph_id))
    all_apis = RechargeApi.objects.all()
    if request.method == 'GET':
        return render_to_response('recharge.html', 
            {'val':ph_numb, 'apis': all_apis}, context_instance=RequestContext(request))
    
    message = "%s"
    api_used = RechargeApi.objects.filter(pk=request.POST.get('api'))

    if not api_used:
        message%"Something went wrong. %s"

    # Check balance
    if request.user.useraccount.balance < 10:
        message%'You dont have enough balance in your account. %s'

    ph_numb.api_used = api_used[0]
    ph_numb.is_successful = rechareresponse()
    if ph_numb.is_successful:
        api_used[0].successful+= 1
        request.user.useraccount.balance-= 10
        request.user.useraccount.save()
        message = 'Recharge Successful.%s'
    else:
        api_used[0].failed+= 1
        message%'Recharge Failed. %s'

    ph_numb.save()
    api_used[0].save()
    context_data = {'val':ph_numb, 'apis': all_apis, 'message':message%''}
    return render_to_response('recharge.html',context_data,
            context_instance=RequestContext(request))






