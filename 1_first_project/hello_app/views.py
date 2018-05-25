from django.shortcuts import render
#from django.http import HttpResponse
from hello_app.models import AccessRecord, Topic, Webpage

# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    webpages_list = AccessRecord.objects.order_by('date')
    dict =  {'templatevar1': "What a beautiful setup!", 'access_records': webpages_list}
    return render(request, 'hello_app/index.html', context = dict)

