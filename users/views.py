from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse, QueryDict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView

from demo.logic import CustomLogicMixin
from users.models import Human


@method_decorator(csrf_exempt, name='dispatch')
class HumanView(CustomLogicMixin, CreateView):
    model = Human
    http_method_names = ['post', 'get']
    content_type = ['multipart/form-data', 'application/json']
    fields = '__all__'
    paginate_by = 3

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            return HttpResponse(status=204)
        else:
            return self.error_response(form.errors.get_json_data())

    def get_objects_by_page(self, page):
        pages_number, query_set = super().get_objects_by_page(page)
        serialized = []
        for entry in query_set:
            temp = model_to_dict(entry)
            temp['avatar'] = entry.avatar.url
            serialized.append(temp)
        return pages_number, serialized


@method_decorator(csrf_exempt, name='dispatch')
class HumanDetailView(UpdateView):
    model = Human
    http_method_names = ['get', 'put', 'delete']
    content_type = ['application/json']

    def get(self, request, *args, **kwargs):
        data = model_to_dict(self.get_object())
        data['avatar'] = data['avatar'].url
        return JsonResponse(data, status=200)

    def put(self, request, *args, **kwargs):
        human = self.model.objects.get(pk=kwargs['pk'])
        for field, value in QueryDict(request.body).items():
            setattr(human, field, value)

        try:
            human.save()
            return HttpResponse(status=204)
        except ValueError as error:
            return self.error_response(error)

    def delete(self, request, *args, **kwargs):
        try:
            self.model.objects.get(pk=kwargs['pk']).delete()
        except ObjectDoesNotExist as error:
            return self.error_response(error, status=410)
