from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from CustomUser.models import CustomUserModel

class SignupSerializer(serializers.ModelSerializer):
	'''
	[Serialize Signup data]
	'''
	email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=CustomUserModel.objects.all())])
	username = serializers.CharField(max_length=32,validators=[UniqueValidator(queryset=CustomUserModel.objects.all())])
	password = serializers.CharField(min_length=8, write_only=True)

	def create(self, data):
		user = CustomUserModel.objects.create_user(data['email'], data['username'],data['password'])
		return user

	class Meta:
		model = CustomUserModel
		fields = ('id', 'username', 'email', 'password','user_token')

class LoginSerializer(serializers.Serializer):
	'''
	[Serialize Login data]
	'''
	username = serializers.CharField(max_length=300, required=True)
	password = serializers.CharField(required=True, write_only=True)

