from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import VideoModel
from .form import UserForm


# Create your views here.

class Index(ListView):
    template_name = 'index.html'
    model = VideoModel


def vrform(request):
    if request.method == 'POST':
        # creating User form class object
        form = UserForm(request.POST)
        if form.is_valid():
            # assigning form data into my model
            new_req = VideoModel(video_title=request.POST['inp_title'],
                                 video_desc=request.POST['inp_desc'])
            new_req.save()
            return redirect('index')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'form.html', context)





