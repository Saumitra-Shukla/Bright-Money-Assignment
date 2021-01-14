from django.urls import path
from CustomUser.views import SignupAPIView,LoginAPIView,LogoutAPIView

urlpatterns = [

    #all are POST based urls
    
    path('api/signup/', SignupAPIView.as_view(), name='User-Signup-API'),
    path('api/login/', LoginAPIView.as_view(), name='User-Login-API'),
    path('api/logout/', LogoutAPIView.as_view(), name='User-Logout-API'),
]