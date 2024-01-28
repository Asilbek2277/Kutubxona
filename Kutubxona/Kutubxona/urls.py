"""
URL configuration for Kutubxona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', all_books),
    path('students/', all_students),
    path('bitiruvchilar/', bitiruvchilar),
    path('talaba/', talaba),
    path('ism/', ism_a),
    path('muallif/', muallif),
    path('muallif_ochirish/<int:pk>/', muallif_ochirish),
    path('bitta_talaba/<int:pk>/', bitta_talaba),
    path('hamma_mualliflar/', hamma_mualliflar),
    path('bitta_muallif/<int:son>/', bitta_muallif),
    path('kitob/', hamma_kitoblar),
    path('bitta_kitob/<int:pk>/', bitta_kitob),
    path('hamma_recordlar/', hamma_recordlar),
    path('recordni_ochirish/<int:pk>/', recordni_ochirish),
    path('tirik_mualliflar/', tirik_mualliflar),
    path('uchta_kitob/', uchta_kitob),
    path('uchta_muallif/', uchta_muallif),
    path('uchta_record/', uchta_record),
    path('t_m_kitoblari/', t_m_kitoblari),
    path('badiiy/', badiiy),
    path('uchta_mu/', uchta_mu),
    path('k_soni/', k_soni),
    path('biron_id/<int:pk>/', biron_id),
    path('bitiruvchi_t_r/', bitiruvchi_t_r),
    path('talaba_ochir/<int:pk>/', talaba_ochir),
    path('kitob_ochirish/<int:pk>/', kitob_ochirish),
    path('kutubxonachilar/', kutubxonachilar),
]
