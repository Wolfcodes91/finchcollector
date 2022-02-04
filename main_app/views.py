from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

finches = [
  Finch('Ryland', 'saffron', 'chill, naps a lot',  3),
  Finch('Mehj', 'blue', 'pretty bird, sips tea', 2),
  Finch('Dave', 'spice', 'spicy-boy, charming', 4),
  Finch('Devlin', 'society', 'high-society', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>FinchCollections</h1>')

def about(request):
   return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })