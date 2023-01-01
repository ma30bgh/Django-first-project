from django.shortcuts import render

# Create your views here.
def home(reqest):
    return render(reqest, 'home.html')

def sey_hello(reqest):
    return render(reqest, 'hello.html')