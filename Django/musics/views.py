from django.shortcuts import render

# Create your views here.
def Hello_django(request):
    return render(request,'hello_django.html',{
        'data':'hello.django',
    })
