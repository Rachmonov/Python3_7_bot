from django.contrib import admin
from myfolder.models import *
# Register your models here.

class AdminUsers(admin.ModelAdmin):
    list_display = ['id','ism','fam','tg_id']

admin.site.register(Users,AdminUsers)



class AdminTurlar(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Turlar,AdminTurlar)


class AdminMaxsulot(admin.ModelAdmin):
    list_display = ['id','nomi','narxi','turi','rasm_url']

admin.site.register(Maxsulot,AdminMaxsulot)


class AdminSavdo(admin.ModelAdmin):
    list_display = ['id','maxsulot_id','tg_id','status','last_date']

admin.site.register(Savdo,AdminSavdo)