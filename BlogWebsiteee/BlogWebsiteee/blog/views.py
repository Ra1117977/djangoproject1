from django.http import HttpResponse
from django.template import loader
def blog(request):
template = loader.get_template('websites.html')
return HttpResponse(template.render())