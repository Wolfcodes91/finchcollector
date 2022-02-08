from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import WatchingForm

# Create your views here.


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
   return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    #instantiate FeedingForm to be rendered in the template
    watching_form = WatchingForm()
    return render(request, 'finches/detail.html', { 
      'finch': finch,
      'watching_form': watching_form,
    })

def add_viewing(request, finch_id):
    form = WatchingForm(request.POST)
    #validate the form
    if form.is_valid():
      # dont save the form to the db until it 
      # has the finch_id assigned
      new_viewing = form.save(commit=False)
      new_viewing.finch_id = finch_id
      new_viewing.save()
    return redirect('detail', finch_id=finch_id)

#class based view
class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['type', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

