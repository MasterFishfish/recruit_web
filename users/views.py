from django.shortcuts import render

# Create your views here.
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from undefined.helpers import JSONResponse, InputErrorMessage
from .models import UserSerialiser, User, PotentialUser

def index(request):
    return render(request, 'loginpage/loginpage.html', {'key': 'value'})

def personalpage(request):
    return render(request, 'personalpage/personalpage.html', {'key': 'value'})

class UserShow(APIView):
    def get(self, request, format=None):
        serializer = UserSerialiser(request.user)
        return Response(serializer.data)


class ChangePassword(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return InputErrorMessage(
                "Invalid JSON body",
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        if "old_password" not in data:
            return InputErrorMessage(
                "You must provide old password",
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        if not request.user.check_password(data["old_password"]):
            return InputErrorMessage(
                "old password not match",
                status=status.HTTP_403_FORBIDDEN
            )
        if "new_password" not in data:
            return InputErrorMessage(
                "You must provide new password",
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        request.user.set_password(data["new_password"])
        request.user.save()
        serializer = UserSerialiser(request.user)
        return Response(serializer.data)


class Register(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        print(request.body.decode('utf-8'))
        print(type(request.body.decode('utf-8')))
        datastr = request.body.decode('utf-8')
        # print("======================")
        # kv = datastr.split('&')
        # datadict = {}
        # for i_kv in kv:
        #     key, value = i_kv.split('=')
        #     datadict[key] = value
        try:
            data = json.loads(datastr)
            # data = json.loads(data)
        except json.JSONDecodeError:
             return InputErrorMessage("Invalid JSON body")
        if "username" not in data:
            return InputErrorMessage("username not provide.")
        if User.objects.filter(username=data["username"]).exists():
            return InputErrorMessage("username is used.")
        if "email" not in data:
            return InputErrorMessage("email not provide.")
        if User.objects.filter(email=data["email"]).exists():
            return InputErrorMessage("email is used.")
        if "password" not in data:
            return InputErrorMessage("password not provide.")
        user = User.objects.create_user(username=data["username"],
                                        email=data["email"], password=data["password"])
        user.save()
        return JSONResponse({
            "code": 200,
            "message": "OK",
        })


class Beta(APIView):
    permission_classes = (AllowAny,)
    """
    希望的输入：(UTF-8 coded)
       {
            "email": "ewre@qq.com",
            "favoritebrowser": "chrome",
            "job": "student"
        }
    """
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return InputErrorMessage("Invalid JSON body")
        if "email" not in data:
            return InputErrorMessage("email not provide")
        if "favoritebrowser" not in data:
            return InputErrorMessage("favoritebrowser not provide")
        if "job" not in data:
            return InputErrorMessage("job not provide")
        potentialuser = PotentialUser.objects.create(email=data["email"],
                                                     favoritebrowser=data["favoritebrowser"],
                                                     job=data["job"])
        potentialuser.save()
        return JSONResponse({
            "code": 200,
            "massage": "OK",
        })