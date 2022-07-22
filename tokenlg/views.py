from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from tokenlg.authentication import create_refresh_access, create_token_access, decode_refresh_access, decode_token_access 
from tokenlg.models import User
from .serializers import UserSerializer
# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        if not user: 
            raise APIException('Invalid Credential')    
        if not user.check_password(request.data['password']):
            raise APIException('Invalid Credential')
        
        token_access = create_token_access(user.id) 
        refresh_access = create_refresh_access(user.id)
        
        response = Response()
        response.set_cookie(key='refreshToken', value=refresh_access, httponly=True)
        response.data = {
            'token': token_access
        }
        return response

class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_token_access(token)
            user = User.objects.filter(pk=id).first()
            return Response(UserSerializer(user).data)
        raise AuthenticationFailed('unauthenticated')

class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_access(refresh_token)
        access_token = create_token_access(id)
        return Response({
            'token': access_token
        })
class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie("refreshToken")
        response.data = {
            "message": "success"
        }
        return response