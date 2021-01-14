from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from CustomUser.serializers import SignupSerializer,LoginSerializer

class SignupAPIView(APIView):
	'''
	[Basic signup view]
	@/api/signup/
	[POST req]
	'''
	def post(self, request):
		serializer = SignupSerializer(data=request.data)
		if serializer.is_valid():
			request.email = serializer.validated_data['email']
			request.username = serializer.validated_data['username']
			request.password = serializer.validated_data['password']
			user = serializer.create(request.data)

			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
	'''
	[Basic Login view]
	@/api/login/
	[POST req]
	'''
	def post(self, request):
		serializer = LoginSerializer(data=request.data)

		if serializer.is_valid():
			username = serializer.validated_data['username']
			password = serializer.validated_data['password']
			user = authenticate(username=username,password=password)
			print(user)
			if user:
				login(request, user)
				token = Token.objects.get_or_create(user=user)
				msg = {'success': 'logged in'}
				return Response(data=msg, status=status.HTTP_200_OK)
			else:
				raise serializers.ValidationError("Invalid username/password.")
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
	'''
	[Basic Logout view]
	@/api/logouts/
	[POST req]
	'''
	authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
	permission_classes = [IsAuthenticated]

	def post(self, request):
		try:
			request.user.auth_token.delete()
		except (AttributeError, ObjectDoesNotExist):
			pass

		logout(request)
		msg = {'success': 'logged out'}
		return Response(data=msg, status=status.HTTP_200_OK)