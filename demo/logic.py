from django.http import JsonResponse


class CustomLogicMixin:
    paginate_by = None
    model = None

    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get('page', 0))
        except ValueError as error:
            return self.error_response(error)

        pages_number, data = self.get_objects_by_page(page)

        if page >= pages_number and len(data) == 0:
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

        number = self.model.objects.count()
        if end >= number:
            end = number
        pages_number = number // self.paginate_by + 1
        if (number < pages_number) or (number == self.paginate_by):
            pages_number = 1

        data = self.model.objects.all()[start:end]

        return pages_number, data

    @staticmethod
    def error_response(msg, status=400):
        response = {"error": str(msg)}
        return JsonResponse(response, status=status)
