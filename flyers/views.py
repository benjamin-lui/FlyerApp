# Create your views here.

from flyers.models import Flyer
from django.http import HttpResponse

def index(request):
	
	return HttpResponse("Hello, world. You're at the poll index.")