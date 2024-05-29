from django.shortcuts import render, HttpResponse

# Create your views here.
def index (request):
    return render(request, 'index.html')

def aboutus (request):
    return render(request, 'aboutus.html')

def contactus (request):
    return render(request, 'contactus.html')

def services (request):
    return HttpResponse("this is service page")

def kentrance (request):
    return render(request, 'kentrance.html')

def kenergy (request):
    return render(request, 'kenergy.html')

def kkeypad (request):
    return render(request, 'kkeypad.html')

def curtainmotors (request):
    return render(request, 'curtainmotors.html')

def alighting (request):
    return render(request, 'alighting.html')

def aaccesscontrol (request):
    return render(request, 'aaccesscontrol.html')

def aaudiovisualcontrolandacoustics (request):
    return render(request, 'aaudiovisualcontrolandacoustics.html')

def asecurityandsurvillence (request):
    return render(request, 'asecurityandsurvillence.html')

def acentralvaccum (request):
    return render(request, 'acentralvaccum.html')

def aventilationsystems (request):
    return render(request, 'aventilationsystems.html')

def faqs (request):
    return render(request, 'faq.html')

def login (request):
    return render(request, 'login.html')

def terms (request):
    return render(request, 'terms.html')

def privacy (request):
    return render(request, 'privacy.html')

def pricing (request):
    return render(request, 'pricing.html')

def readmore (request):
    return render(request, 'readmore.html')

