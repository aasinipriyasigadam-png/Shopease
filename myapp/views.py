from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.http import  JsonResponse
from django.contrib.auth.models import User
from .models import Products, Cart , Orders

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homepage(request):
    products=Products.objects.all()
    print(products,"----------------")
    return render(request,'home.html',context={'items': products})



def registerpage(request):
    print(request.method,"I")
    if request.method =='GET':
        return render(request,'register.html')
    elif request.method =='POST':
        data=request.POST
        print(data)

        first_name = data['First_Name']
        last_name = data['Last_Name']
        pwd = data['pwd']
        conf_pwd = data['conf_pwd']
        email = data['email']

        # user registration
        if pwd != conf_pwd:
            return render(request,'register.html', context={"error": "passwords not matching!"})

        users = User.objects.filter(username=email) # this will give list

        if len(users) > 0:
            return render(request,'register.html', context={"error": "User already exist!"})

        # if user does not exist create a new user
        new_user  = User.objects.create(first_name = first_name, 
                                        last_name=last_name, 
                                        username=email,
                                        email=email)
        new_user.set_password(pwd)
        new_user.save()

        return redirect("login-page")


def loginpage(request):
    print(request.method, "I am login")
    if request.method=='GET':
        if request.user.is_authenticated: 
            return redirect("products-home")
        return render(request,'login.html')
    elif request.method=='POST':
        data=request.POST
        # user check
        username = data.get('username', '')
        pwd = data.get('pwd', '')
        users = User.objects.filter(username=username)
        if len(users)<1:
            return render(request,'login.html', context={"error": "user does not exist"})
        # first user existed
        user = users[0]
        # password is correct
        valid = user.check_password(pwd)
        if not valid:
            return render(request,'login.html', context={"error": "invalid password"})
        login(request, user)
        
        # login 
        return redirect('products-home')



def products(request):
    products = list(Products.objects.all().values())
    return JsonResponse({"prodcuts": products})  

def product_by_id(request, product_id):
    products = list(Products.objects.filter(id=product_id).values())
    return JsonResponse({"products": products})

@csrf_exempt
def cartpage(request, product_id=None):
    print(request.method,"I")
    if request.user.is_authenticated: 
        if request.method =='GET':
            cart = Cart.objects.filter(user=request.user)

            ls = []
            for item in cart:
                product={
                    "price":item.product_id.price,
                    "name":item.product_id.name,
                    "image":item.product_id.image,
                    "count":item.count
                    }
                ls.append(product)
            print(ls)
            return render(request,'cart.html',context={'cart_items': ls})
        elif request.method =='POST':
        # check prodcut id
            aval_prods  = Products.objects.filter(id=product_id).first()

        # check the same product is already in the cart
            cart_items = Cart.objects.filter(product_id=aval_prods, user=request.user)
            print(cart_items, )
            if len(cart_items) > 0:
                cart_item = cart_items.first()
                cart_item.count += 1
                cart_item.save()
            else:
                c = Cart.objects.create(user=request.user, product_id=aval_prods)
                c.save()
                print("product saved....")
        # if the product already exists in cart, just update the count
        # else just create cart object
    return redirect("products-home")

@csrf_exempt
def orderspage(request, product_id=None):
    # print(request.method,"I")
    if request.user.is_authenticated: 
        if request.method =='GET':
            orders = Orders.objects.filter(user=request.user).order_by('-order_date')

            ls=[]
            for item in orders:
                product={
                    "id":item.product_id.id,
                    "price":item.product_id.price,
                    "date":item.order_date,
                    "name":item.product_id.name,
                    "image":item.product_id.image,
                }
                ls.append(product)
            print(ls)
            return render(request,'orders.html',context={'ordered_items':ls})
        elif request.method =='POST':
            aval_prods =Products.objects.filter(id=product_id).first()
            ordered_items = Orders.objects.filter(product_id=aval_prods,user=request.user)
            # print(ordered_items, )
            c = Orders.objects.create(user=request.user,product_id=aval_prods)
            c.save()
            # print("product saved")
            return JsonResponse({"status": True})
    return redirect("login-page")  

         
def user_logout(request):
    logout(request)
    return redirect("login-page")