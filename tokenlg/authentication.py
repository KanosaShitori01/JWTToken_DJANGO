from rest_framework import exceptions
import jwt, datetime
def create_token_access(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        'iat': datetime.datetime.utcnow() 
    }, 'access_secret', algorithm="HS256")
def decode_token_access(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms="HS256")
    
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
        
def create_refresh_access(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm="HS256")
def decode_refresh_access(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms="HS256")
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')