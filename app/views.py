from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from app.forms import SchoolForm
from django.http import HttpResponse



class Temp(TemplateView):
    template_name="Temp.html"

    def get_context_data(self, **kwargs):
        ECDO= super().get_context_data(**kwargs)
        #ECDO['name']='Vruta'
        ECDO['SFO']=SchoolForm
        return ECDO
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse("Data inserted successfully")


    


