from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json 

def index(req):
  return JsonResponse({'Api Message': 'Hello from API!'})

@csrf_exempt
def summoner(request):
  if request.method == 'POST':
    name = request.POST
    # name = request.body.decode('utf-8')
    # body = json.loads(name)
    # name = body['name']
    content = {'Post':name}
    return render(request,'base/index.html',content)
    return JsonResponse({'Post': name})
    return JsonResponse({'Name': request.method})
  else:
    return JsonResponse({'name':'skata'})
