from django.shortcuts import render
from .models import testAppVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_testApp(request):
    apps = testAppVariety.objects.all()
    return render(request, 'testApp/all_testApp.html', {'apps': apps})

def app_detail(request, app_id):
    app = get_object_or_404(testAppVariety, pk=app_id)
    return render(request, 'testApp/app_detail.html', {'app': app})
