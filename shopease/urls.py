"""
URL configuration for shopease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import(homepage,registerpage,loginpage,cartpage,orderspage,product_by_id, user_logout)
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",homepage),
    path('home',homepage, name='products-home'),
    path("register/",registerpage),
    path("login",loginpage),
    path('login/',loginpage, name="login-page"),
    path("cart",cartpage),
    path('cart/<int:product_id>/',cartpage),
    path("orders",orderspage),
    path('orders/<int:product_id>/',orderspage),
    path('products/<int:product_id>/',product_by_id),
    path('logout', user_logout)

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
