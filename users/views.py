from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse, QueryDict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView

from users.models import Human


@method_decorator(csrf_exempt, name='dispatch')
class HumanView(CreateView):
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
            return HttpResponse(status=400)

    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get('page', 0))
        except ValueError:
            return self.error_response("page must be integer")

        pages_number, data = self.get_objects_by_page(page)

        if page > pages_number and len(data) == 0:
            return self.error_response("page out of range")

        response = {
            "page": page,
            "pages_number": pages_number,
            "data": data,
        }
        return JsonResponse(response, status=200)

    def get_objects_by_page(self, page):
        start = page * self.paginate_by
        end = (page + 1) * self.paginate_by

        number = Human.objects.count()
        if end >= number:
            end = number
        pages_number = number // self.paginate_by + 1
        if (number < pages_number) or (number == self.paginate_by):
            pages_number = 0

        data = Human.objects.all()[start:end]
        return pages_number, list(data.values())

    def error_response(self, msg):
        response = {"error": msg}
        return JsonResponse(response, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class HumanDetailView(UpdateView):
    model = Human
    http_method_names = ['get', 'put']
    content_type = ['application/json']

    def get(self, request, *args, **kwargs):
        data = model_to_dict(self.get_object())
        data['avatar'] = data['avatar'].url
        return JsonResponse(data, status=200)

    def put(self, request, *args, **kwargs):
        object = self.model.objects.get(pk=kwargs['pk'])
        for field, value in QueryDict(request.body).items():
            setattr(object, field, value)

        try:
            object.save()
            return HttpResponse(status=204)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
