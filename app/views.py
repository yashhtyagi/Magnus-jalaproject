from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import ImageUpload
from django.contrib import messages

# Create your views here.
@login_required(login_url="/")
def home(request):
    return render(request, 'app/home.html')

@login_required(login_url="/")
def images(request):
    form = ImageForm()
    images = ImageUpload.objects.all()
    if request.method == 'POST':
        form = ImageForm(files=request.FILES,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Image Uploded Successfully")
            return redirect('images')
        else:
            messages.error(request, "Error occured while uploading")
            return redirect('images')

    context = {'form': form, 'images': images}
    return render(request, 'app/images.html', context)


def tabs(request):
    return render(request, 'app/MultipleTabs.html')

def menu(request):
    return render(request, 'app/Menu.html')

def autocomplete(request):
    return render(request, 'app/Autocomplete.html')

def collapsiblecontent(request):
    return render(request, 'app/CollapsibleContent.html')

def slider(request):
    return render(request, 'app/Slider.html')

def tooltip(request):
    return render(request, 'app/Tooltips.html')

def popups(request):
    return render(request, 'app/Popups.html')

def links(request):
    return render(request, 'app/Links.html')

def cssproperties(request):
    return render(request, 'app/CSSProperties.html')

def iframe(request):
    return render(request, 'app/iFrames.html')

def page_404(request):
    return render(request, 'app/404.html')

def page_500(request):
    return render(request, 'app/500.html')

def page_301(request):
    return render(request, 'app/300.html')