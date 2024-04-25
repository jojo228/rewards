from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):

    products = Products.objects.all()[0:3]
    
    return render(request, "index.html", locals())


def errorpage(request):
    
    return render(request, "404.html")


def about(request):
    
    return render(request, "about.html")


def contacts(request):
    
    return render(request, "contact-2.html")


def project(request):
    
    return render(request, "project.html")

def faq(request):
    
    return render(request, "faq.html")


######## SERVICES ########
def service(request):
    
    return render(request, "services-1.html")

def service_details(request):
    
    return render(request, "service-details.html")


def team(request):
    
    return render(request, "team.html")



def testimonial(request):
    
    return render(request, "testimonial.html")



def blogsingle(request):
    
    return render(request, "blog-single.html")

def blog(request):
    
    return render(request, "blog.html")


######## PRODUCTS ########
def products(request):

    products = Products.objects.all()
    
    return render(request, "products.html", locals())

def product_details(request, pk):

    product = Products.objects.get(id=pk)
    products = Products.objects.all()[0:6]
    
    return render(request, "product-details.html", locals())


