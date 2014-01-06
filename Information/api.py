from .serializer import *
from .models import *
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User


class PhoneNumberList(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = PhoneNumber.objects.all()
        user = self.request.user
        return queryset.filter(added_by=user)

    def pre_save(self, obj):
        #todo--remove this operator hardcoding
        obj.operator_id = 1
        obj.added_by = self.request.user


class PhoneNumberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OperatorList(generics.ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = UserAccount.objects.all()
        user = self.request.user
        return queryset.filter(account=user)


class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

