from django.contrib import admin
from .models import Services, Contact

admin.site.register((Services, Contact))
