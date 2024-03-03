from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.utils import get_md5_hash_password
from core.models import User
from django.conf import settings


class customJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
            header = self.get_header(request)
            if header is None:
                return None
            raw_token = header.decode('utf-8').split(' ')[1]
            if raw_token is None:
                return None
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), validated_token
     
    def get_user(self, validated_token):
        try:
            user_id = validated_token[settings.SIMPLE_JWT["USER_ID_CLAIM"]]
        except KeyError:
            raise InvalidToken(_("Token contained no recognizable user identification"))
        try:
            user = User.objects.get(id=user_id)
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed(_("User not found"), code="user_not_found")

        if not user.is_active:
            raise AuthenticationFailed(_("User is inactive"), code="user_inactive")

        if settings.CHECK_REVOKE_TOKEN:
            if validated_token.get(
                settings.REVOKE_TOKEN_CLAIM
            ) != get_md5_hash_password(user.password):
                raise AuthenticationFailed(
                    _("The user's password has been changed."), code="password_changed"
                )

        return user



