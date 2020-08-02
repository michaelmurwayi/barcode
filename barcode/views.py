from django.views.generic.base import TemplateView
from django.core.files.storage import FileSystemStorage
from .bar_reader import get_barcode_data
import os
from django.conf import settings 
from django.shortcuts import render, redirect



class HomeView(TemplateView):
    template_name = "index.html"


    def post(self, request):
        files = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(files.name, files)
        uploaded_file_path = os.path.join( 'media/', filename)
        data = get_barcode_data(uploaded_file_path)
        context = {
            "data":data
        }
        return render(request, "index.html", {"context":context} )