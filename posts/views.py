from django.shortcuts import render
from .models import Enquiry
from . import forms
from .forms import Enquiry

def enquiryform(request, *args, **kwangs):
    form = Enquiry(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = Enquiry()
    return render(request, 'posts/enquiryform.html',{'form': form})
