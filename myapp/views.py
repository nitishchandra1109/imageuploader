from django.shortcuts import render,HttpResponseRedirect
from .forms import ImageForm
from .models import Image
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html',{'form':form,'img':img })


def delete_img(request,id):
    if request.method =='POST':
        im = Image.objects.get( pk =id )
        im.delete()
        return HttpResponseRedirect('/')