import secrets
import string
from rest_framework_simplejwt.tokens import RefreshToken

def generate_random_string(length=10):
    # Define the characters to choose from
    alphabet = string.ascii_letters + string.digits
    
    # Generate the random string
    random_string = ''.join(secrets.choice(alphabet) for i in range(length))
    
    return random_string


def get_tokens(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }