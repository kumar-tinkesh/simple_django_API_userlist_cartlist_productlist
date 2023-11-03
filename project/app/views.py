from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from .models import RegistrationData, product,cart

# Create your views here.

def registration_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Validate and process data here as needed

        # Create an instance of the model and save it
        registration_data = RegistrationData(name=name, email=email, phone=phone, password=password)
        registration_data.save()

        return redirect('index')  # Redirect to a success page

    return render(request, 'registration.html')



# users = RegistrationData.objects.all()
# for user in users:
#     print(user.name, user.email, user.password, user.phone)



def login_view(request):
    if request.method == 'POST':
        input_email = request.POST.get('email')
        input_password = request.POST.get('password')
        user = request.POST.get('name')
        
        matching_users = RegistrationData.objects.filter(email=input_email, password=input_password)

        if matching_users.exists():
            user = matching_users.first()
            return HttpResponse(f"User Found for given Email or Password: {user.name}")
            return redirect('index')
        else:
            
            return HttpResponse("Email and password not found in the database")

    return render(request, 'login.html')



# we display product in html page one by one 

def product_view(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        brand = request.POST.get('brand')
        category = request.POST.get('category')
        rating = request.POST.get('rating')


        product_data = product(title=title, description=description, price=price, discount=discount, brand=brand, category=category,rating=rating)
        product_data.save()

        return redirect('index')  # Redirect to a success page

    return render(request, 'product.html')



# we display all product in html page

# def product_list(request):
#     products = product.objects.all()
#     return render(request, 'product_list.html', {'products': products})


# def add_to_cart(request):
#     products = product.objects.all()
#     for item in products:
#         cart_data = cart(
#             title = item.title,
#             brand = item.brand,
#             price = item.price,
#         )
#         cart_data.save()
#     return render(request, 'cart.html', {'products': products}) 
#     # return HttpResponse("hi")



def add_to_cart(request):
    products = product.objects.all()
    cart_items = []
    for item in products:
        cart_data = {
            'title' : item.title,
            'brand' : item.brand,
            'price' : item.price,
        }
        # cart_data.save()
        cart_items.append(cart_data)
    return JsonResponse({'cart_items': cart_items}, safe=False)




# plist = product.objects.all()
# for p in plist:
#     print(p.title, p.description, p.price, p.brand)


def get_product_list(request):
    p_list = product.objects.all()
    p_data = [{'title':p.title,'description':p.description, 'price':p.price, 'brand':p.brand} for p in p_list]
    return JsonResponse({'p_list': p_data}, safe=False)


# def get_product_list(request):
#     p_list = product.objects.all()
#     p_data = [{'title':p.title,'description':p.description, 'price':p.price, 'brand':p.brand, 'discount':p.discount, 'category':p.category, 'rating':p.rating} for p in p_list]
#     return render(request, 'product_list.html',{'p_list':p_data})




# def get_user(request):
#     users = RegistrationData.objects.all()
#     user_data = [{'name':user.name,'email':user.email, 'password':user.password, 'phone':user.phone} for user in users]
#     return JsonResponse({'users': user_data}, safe=False)



def get_user(request):
    users = RegistrationData.objects.all()
    user_data = [{'name':user.name,'email':user.email, 'password':user.password, 'phone':user.phone} for user in users]
    return render(request, 'user_list.html',{'users':user_data})






# def compare_email():
#     input_email = input("Enter your email : ")
#     input_pwd = input("Enter your pwd : ")
#     try:
#         user = RegistrationData.objects.get(email=input_email)
#         user = RegistrationData.objects.get(password=input_pwd)

#         print(f"Name found: {user.name}")
#     except RegistrationData.DoesNotExist:
#         print("Email not found in the database")

# compare_email()


def index(request):
        return render(request, 'index.html')


def home(request):
        return render(request, 'home.html')