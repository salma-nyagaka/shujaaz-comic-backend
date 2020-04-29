
# import Http Response from django 
from django.shortcuts import render 
   
# create a function 
def home_view(request):  
    return render(request, "index.html") 
