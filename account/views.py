from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer, ChangePasswordSerializer, \
    ForgotPasswordSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            Вы успешно зарегистрировались!
            Вам отправлено письмо c кодом активации.
            """
            return Response(message)


class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Вы успешно активированы')


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно вышли')


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create_new_password()
            return Response('Вам на почту выслан новый пароль')



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(dat=request.data,
                                              context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлен')





#REST

# 1. Model client -server / Server za eto ne otvechaet. Vse delaetsya na

# 2. Otsutstvie sostoyanie klienta / Kajdy raz doljen otpravlyat s klyuchom

# 3. Keshirovanie - promejutochnaya baza dannyh

# 4. Edinobrazie interfeisa - vse viewshki doljny rabotat odinakovym obrazom i v odnom stile

# 5. Sistema sloev - vse chto proishodit vnutri posle zaprosa klientu ne obyazatelno znat

# 6. Kod po trebovaniyu (neobyazatelno)

