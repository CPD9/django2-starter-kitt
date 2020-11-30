from django.shortcuts import render

# Create your views here.
# function below handle requests passed along by _djproject/url
def home_view(request):
    return render(request, 'allpages/base.html',{'title': 'Home'})

def about_view(request):
    return render(request, 'allpages/index.html',{'title': 'About Us'})
    
def privacy_view(request):
    return render(request, 'allpages/privacy.html', {'title': 'Privacy Policy'})

