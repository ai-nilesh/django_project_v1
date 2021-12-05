
from django.views.generic import ListView, TemplateView,DetailView
from . models import BlogModal


# Create your views here.
class HomePageVIew(ListView):
    template_name = 'home.html'

    model = BlogModal


class AboutPageVIew(TemplateView):
    template_name = 'about.html'


class ContactPageVIew(TemplateView):
    template_name = 'contact.html'

class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = BlogModal
    context_object_name = 'post'


