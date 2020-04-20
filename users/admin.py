from django.contrib import admin

from match.models import Match
from users.models import Human

admin.site.register(Human)
admin.site.register(Match)
