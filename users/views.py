from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from users.models import Human


@method_decorator(csrf_exempt, name='dispatch')
class HumanCreateView(CreateView):
    model = Human
    http_method_names = ['post', 'get']
    content_type = 'multipart/form-data'
    fields = '__all__'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=400)
