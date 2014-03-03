from django.shortcuts import render

from annoying.decorators import render_to

# Create your views here.


@render_to('base/index.html')
def index(request):
  return {}
