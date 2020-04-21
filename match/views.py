from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic import CreateView, DetailView

from demo.logic import CustomLogicMixin
from match.models import Match


class MatchDetailView(DetailView, CustomLogicMixin):
    model = Match
    http_method_names = ['get']
    content_type = ['application/json']

    def get(self, request, *args, **kwargs):
        try:
            data = model_to_dict(self.model.objects.get(human_id=kwargs['human_id']))
        except ObjectDoesNotExist as error:
            return self.error_response(error, status=404)
        return JsonResponse(data, status=200)


class MatchListView(CustomLogicMixin, CreateView):
    model = Match
    http_method_names = ['get']
    content_type = ['application/json']
    fields = '__all__'
    paginate_by = 3

    def get_objects_by_page(self, page):
        pages_number, query_set = super().get_objects_by_page(page)
        return pages_number, list(query_set.values())
