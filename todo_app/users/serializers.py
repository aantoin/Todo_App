import re

from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    def save(self, request):
        user = super().save(request)
        if user and user.email and True:
            print(
                "!!!!!!!!!!!",
                re.fullmatch(
                    user.email, r"guest-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}@test\.com"
                ),
            )
            print("!!!!!!!!!!!", user.email, user.emailaddress_set.filter(email=user.email).first())
            email = user.emailaddress_set.filter(email=user.email).first()
            email.verified = True
            email.save()
        else:
            print("!!!!!!!!!!! NO USER!!!")
        return user
