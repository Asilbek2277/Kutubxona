from django.contrib import admin

from .models import *

class TalabaAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "kurs", "kitob_soni"]
    list_display_links = ["ism"]
    list_editable=["kurs"]
    list_filter=["kurs"]
    search_fields = ["id", "ism"]
    search_help_text = "Id va ism bo'yicha qidiring"
    list_per_page = 2



class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "jins", "tugilgan_sana", "Kitoblar_soni", "tirik"]
    list_editable = ["Kitoblar_soni", "tirik"]
    list_filter = ["tirik"]
    list_display_links = ["id", "ism"]
    search_fields = ["ism"]
    search_help_text = "Ism bo'yicha qidiruv"


class KitobAdmin(admin.ModelAdmin):
    list_display = ["id", "nom", "janr", "sahifa", "muallif"]
    list_display_links = ["nom"]
    list_editable = ["sahifa"]
    search_fields = ["nom", "id", "muallif__ism"]
    list_filter = ["janr", "muallif"]
    autocomplete_fields = ["muallif"]

class KutubxonachiAdmin(admin.ModelAdmin):
    list_filter = ["ish_vaqti"]
    search_fields = ["ism"]
    search_help_text = "Ism b'yicha qidiruv"


class RecordAdmin(admin.ModelAdmin):
    list_display = ["talaba", "Kitob", "kutubxonachi", "olingan_sana", "qaytardi", "qaytarish_sana"]
    autocomplete_fields = ["talaba", "Kitob", "kutubxonachi"]
    search_fields = ["talaba__ism", "Kitob__nom", "kutubxonachi__ism"]


admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob, KitobAdmin)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Record, RecordAdmin)



