from django.urls import path,include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'reg',getRegisterViewset)

urlpatterns = [
    # path('ngoRegister/', include(router.urls)),
    path('getfav/',favNgo.as_view()),
    path('home/',home),
]