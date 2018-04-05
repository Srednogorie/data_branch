from rest_framework import authentication


class MyAuthentication(authentication.BasicAuthentication):
    def authenticate_header(self, request):
        return 'FormBased'