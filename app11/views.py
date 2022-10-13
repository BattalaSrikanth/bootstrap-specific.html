import re
from django.shortcuts import render

# Create your views here.
def man(request):
    return render(request,'flower.html')