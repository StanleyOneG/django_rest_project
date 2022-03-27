from django.http import JsonResponse

# Create your views here.
def home_view(request):
    return JsonResponse({'info': 'Django React Course', 'name': 'stas'})
