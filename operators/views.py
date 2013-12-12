from models import Operator

def which_operator():
    return Operator.objects.order_by('?')[0]
