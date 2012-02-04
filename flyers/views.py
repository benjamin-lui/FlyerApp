# Create your views here.

from django.template import Context, loader
from flyers.models import Flyer
from django.http import HttpResponse

def index(request):
    latest_flyer_list = Flyer.objects.all()
    t = loader.get_template('flyers/index.html')
    c = Context({'latest_flyer_list': latest_flyer_list,})
    return HttpResponse(t.render(c))