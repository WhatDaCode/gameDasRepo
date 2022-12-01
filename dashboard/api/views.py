from django.http import JsonResponse

def index(req):
  return JsonResponse({'Api Message': 'Hello from API!'})