from django.http import HttpResponse, Http404

def landing(request):
	return HttpResponse('Hello. Nice to meet us? Likewyss')
