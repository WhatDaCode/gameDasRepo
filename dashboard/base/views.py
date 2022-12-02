from django.shortcuts import render
from django.http import HttpResponse


# Testing purposes only
accounts = [
    {
        "id":"213123",
        "summonerName":"ARNHTHS DRAKE",
        "level":243,
        "tier":"Bronze",
        "rank":"I"
    },
    {
        "id":"91919",
        "summonerName":"Noliferx DRAKE",
        "level":192,
        "tier":"Silver",
        "rank":"I"
    }
]

def index(request):
  context = {
    'accounts' : accounts
  }
  return render(request, 'base/index.html', context)

def about(request):
  return render(request, 'base/about.html')