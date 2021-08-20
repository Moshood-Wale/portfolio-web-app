# from myenv.projects.models import Works
# from myenv.projects.models import Works
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from .models import Works
# Create your views here.


def index(request):
    roles = Works.objects

    return render(request, 'projects/index.html', {'roles':roles})

def detail(request, role_id):
    
    role_detail = get_object_or_404(Works,pk=role_id)
    return render(request, 'projects/detail.html',{'role':role_detail})
    