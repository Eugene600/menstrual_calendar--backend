from django.urls import path
from .views import UserSignupView, UserLoginView ,UserDetailView, UserEditView, UserDeleteView, UserLogoutView, CustomTokenVerifyView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),  # Login and get tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),  # Verify token validity
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/<str:user_id>/', UserDetailView.as_view(), name='user-detail'), 
    path('user/edit/<str:user_id>/', UserEditView.as_view(), name='user-edit'), 
    path('user/delete/<str:user_id>/', UserDeleteView.as_view(), name='user-delete'), 
]
