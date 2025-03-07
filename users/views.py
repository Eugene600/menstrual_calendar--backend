from django.http import Http404
from .models import CustomUser
from rest_framework.decorators import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.serializers import TokenVerifySerializer

# Create your views here.
class UserSignupView(generics.CreateAPIView):
    """
    Handling user signup.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # Allow anyone to access this view
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # Generate JWT tokens that is access and refresh tokens
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            response_data = {
                'user': serializer.data,
                'tokens': {
                    'access': str(access),
                    'refresh': str(refresh),
                }
            }

            return Response(response_data, status=status.HTTP_201_CREATED)  
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
              
class UserLogoutView(APIView):
    """
    Handle user logout.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            #Get the refresh token from the request
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist() # Blacklist the refresh token

            return Response({"message: Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
   
# Retrieve User Info View
class UserDetailView(generics.RetrieveAPIView):
    """
    Retrieve user info.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user_id'
    
    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({"message: User Does not Exist"}, status=status.HTTP_404_NOT_FOUND)

# Edit User View
class UserEditView(generics.UpdateAPIView):
    """
    Class-based view to handle editing user information.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user_id'
 
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False) # Allow partial updates (PATCH requests)
            instance = self.get_object()
            
            # Get the serializer with tset_passwordhe instance (current user)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            
            return Response({
                'message':'User credentials successfully updated',
                'user': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"message: User Does not Exist"}, status=status.HTTP_404_NOT_FOUND)

# Delete User View
class UserDeleteView(generics.DestroyAPIView):
    """
    Class-based view to handle deleting the user account.
    """
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'user_id'
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            
            return Response({
                'message': 'User successfully deleted'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Exception({"error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#Veryfing access tokens        
class CustomTokenVerifyView(TokenVerifyView):
    serializer_class = TokenVerifySerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            return Response({"message: Access token is valid"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message: Invalid Access Token."}, status=status.HTTP_401_UNAUTHORIZED)


