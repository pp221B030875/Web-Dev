from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Category)
