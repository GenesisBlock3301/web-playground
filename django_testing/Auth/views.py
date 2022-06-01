from rest_framework import viewsets, response, status
from Auth.models import UserAccount
from Auth.Serializeres.user_serializer import UserSerializer, UserRegisterSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = UserAccount.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = UserAccount.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserRegistrationViewset(viewsets.ModelViewSet):
    # queryset = UserAccount.objects.all()
    # serializer_class = UserRegisterSerializer
    

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_registration(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_registration(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


