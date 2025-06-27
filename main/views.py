import json 
from django.conf import settings
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, logout



def login_view(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")

      
        user = authenticate(username=username,password=password)
        if user:
            response = JsonResponse({"msg":"ok"},status=200)
            response.set_cookie(
                key="auth_key",
                value=settings.KEY,
                httponly=True,
                secure=True,
                samesite="Strict"
            )

            return response
        else:
            return JsonResponse({"msg":"invalid username or password"},status=401)
      



def logout_view(req):
    try:
       logout(req)
       response = JsonResponse({"msg":"logged out"})
       response.delete_cookie('auth_key')
       return response
    except Exception:
        print(Exception)
        return JsonResponse({"msg":"error in 32row "},status=500)



