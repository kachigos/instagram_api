from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import GenericAPIView
from .send_email import send_reset_password


User = get_user_model()

class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Account created', 201)

class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully logged out!', status=204)


class ForgotPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(email=serializer.data.get('email'))
            # user.create_activation_code()
            user.save()
            send_reset_password(user)
            return Response('Check your mail!', status=200)
        except User.DoesNotExist:
            return Response('User with this email does not exist!', status=400)

# class ActivationView(APIView):
#     permission_classes = (permissions.AllowAny,)
#
#     def get(self, request, activation_code):
#         try:
#             user = User.objects.get(activation_code=activation_code)
#             user.is_active = True
#             user.activation_code = ''
#             user.save()
#             return Response({
#                 'msg': 'Successfully activated!'},
#                 status=200)
#         except User.DoesNotExist:
#             return Response(
#                 {'msg': 'Link expired!'},
#                 status=400
#             )