from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Muallim,News,Loyihalar,Tadbirlar,Talaba,Izohlar,Registr,Salohiyat

# admin.site.register(Muallim)

@admin.register(Muallim)
class MuallimAdmin(admin.ModelAdmin):
    list_display = ['ismi','slug']
    prepopulated_fields = {'slug':('ismi',)}

    # slugni avtomatik to'ldirish keyinchali

admin.site.register(Salohiyat)
admin.site.register(News)
admin.site.register(Loyihalar)
admin.site.register(Tadbirlar)
admin.site.register(Talaba)
admin.site.register(Izohlar)
admin.site.register(Registr)


class MyModelAdmin(admin.ModelAdmin):
    # ...
    fieldsets = [
        ("Section title", {
            "classes": ("collapse", "expanded"),
            "fields": (...),
        }),
    ]
    # ...
# Register your models here.
