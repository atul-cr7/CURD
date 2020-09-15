from django.contrib import admin
from .models import Data

# Register your models here.
@admin.register(Data)
class Dataadmin(admin.ModelAdmin):
    list_display = ('id','Name','Email','Password')