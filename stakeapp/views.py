from django.shortcuts import render
from .models import Blog, Inquiry
from django.http import JsonResponse

def home(request):
    threeBlogs = Blog.objects.all().order_by('date')[:3]
    context = {'blogs':threeBlogs}
    return render(request, 'home.html', context)

def blog(request):
    context = {'blog':'blogs'}
    return render(request, 'blog.html', context)

def contact(request):
    context = {'blog':'blogs'}
    return render(request, 'contact.html', context)

def inquiry(request):
    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        inquiryObject = Inquiry.objects.create(subject=subject, email=email, message=message)
        return JsonResponse({"message":"success"}, safe=False)
    else:
        return JsonResponse("Method Not allowed", safe=False)

def blogByName(request, name):

    print("dssaawd", name.replace('_', ' '))
    blogName = name.replace('_', ' ')
    blog = Blog.objects.get(title=blogName)
    
    context = {'blog':blog}
    return render(request, 'blog.html', context)