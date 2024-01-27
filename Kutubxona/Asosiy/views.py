from django.shortcuts import render, redirect

from .models import *



def all_books(request):
    if request.method=="POST":
        Kitob.objects.create(
            nom=request.POST.get("nomi"),
            janr=request.POST.get("janr"),
            sahifa=request.POST.get("sahifa"),
            muallif=Muallif.objects.get(id=request.POST.get("mualliflar")),
        )
        return redirect("/books/")
    data={
        "mualliflar": Muallif.objects.all(),
        "books": Kitob.objects.all()
    }
    return render(request, 'kitoblar.html', data)



def all_students(request):
    if request.method == "POST":
        Talaba.objects.create(
            ism=request.POST.get("ismi"),
            kurs=request.POST.get("k"),
            kitob_soni=request.POST.get("k_soni"),
        )
        return redirect("/students/")

    natija=Talaba.objects.all()

    kiritilgan_ismi=request.GET.get("ismi")


    if kiritilgan_ismi is not None:
        natija=Talaba.objects.filter(ism__contains=kiritilgan_ismi)
    data={
        "students":natija
    }
    return render(request, "Students.html", data)





def bitiruvchilar(request):
    data={
        "bitiruvchilar": Talaba.objects.filter(kurs=4)
    }
    return render(request, "Bitiruvchilar.html", data)

def talaba(request):
    data={
        "bitiruvchilar": Talaba.objects.filter(kitob_soni__gt=0)
    }
    return render(request, "Bitiruvchilar.html", data)

def ism_a(request):
    data={
        "bitiruvchilar": Talaba.objects.filter(ism__contains="a")
    }
    return render(request, "Bitiruvchilar.html", data)

def muallif(request):
    if request.method=="POST":
        Muallif.objects.create(
            ism=request.POST.get("ismi"),
            jins=request.POST.get("jins"),
            tugilgan_sana=request.POST.get("date"),
            Kitoblar_soni=request.POST.get("kitob"),
            tirik=False,
        )
        return redirect("/muallif/")
    data={
        "mualliflar": Muallif.objects.all()
    }
    return render(request, "Mualliflar.html", data)



def muallif_ochirish(request, pk):
    Muallif.objects.get(id=pk).delete()
    return redirect("/muallif/")


def ikkinchi_talabalar(request):
    data={
        "students": Talaba.objects.filter(kurs=2)
    }
    return render(request, "Students.html", data)


def bitta_talaba(request, pk):
    data={
        "student": Talaba.objects.get(id=pk)
    }
    return render(request, "Bitta_talaba.html", data)


def hamma_mualliflar(request):
    natija=Muallif.objects.all()
    muallif_ismi=request.GET.get("muallif_ismi")
    if muallif_ismi is not None:
        natija=Muallif.objects.filter(ism__contains=muallif_ismi)
    data={
        "mualliflar": natija
    }
    return render(request, "Mualliflar.html", data)



def bitta_muallif(request, son):
    data={
        "m": Muallif.objects.get(id=son)
    }
    return render(request, "Bitta_muallif.html", data)


def hamma_kitoblar(request):

    natija=Kitob.objects.all()

    kitob_nomi=request.GET.get("nomi")

    if kitob_nomi is not None:
        natija=Kitob.objects.filter(nom__contains=kitob_nomi)
    data={
        "books": natija
    }
    return render(request, "kitoblar.html", data)

def bitta_kitob(request, pk):
    data={
        "kitob": Kitob.objects.get(id=pk)
    }
    return render(request, "Bitta_kitob.html", data)


def hamma_recordlar(request):
    natija=Record.objects.all()
    kiritilgan_ism=request.GET.get("talaba_ismi")
    if kiritilgan_ism is not None:
        natija=Record.objects.filter(talaba__ism__contains=kiritilgan_ism)
    data={
        "record": natija
    }
    return render(request, "Records.html", data)

def recordni_ochirish(request, pk):
    Record.objects.get(id=pk).delete()
    return redirect("/hamma_recordlar/")


def tirik_mualliflar(request):
    data={
        "mualliflar": Muallif.objects.filter(tirik=True)
    }
    return render(request, "Mualliflar.html", data)



kitoblar=Kitob.objects.order_by("-sahifa")
def uchta_kitob(req):
    d={
        "kitob": kitoblar[0:3]
    }
    return render(req, "3kitob.html", d)


mualliflar=Muallif.objects.order_by("-Kitoblar_soni")
def uchta_muallif(req):
    d={
        "muallif": mualliflar[0:3]
    }
    return render(req, "3_muallif.html", d)

recordlar=Record.objects.order_by("-olingan_sana")
def uchta_record(req):
    d={
        "rec": recordlar[0:3]
    }
    return render(req, "3_record.html", d)


def t_m_kitoblari(r):
    d={
        "kitoblar": Kitob.objects.filter(muallif__tirik=True)
    }
    return render(r, "trik_mualliflar_kitoblari.html",d)

def badiiy(r):
    d={
        "kitoblar": Kitob.objects.filter(janr="Badiiy")
    }
    return render(r, "Badiiy_kitoblar.html",d)



yosh=Muallif.objects.order_by("tugilgan_sana")
def uchta_mu(req):
    d={
        "muallif": yosh[0:3]
    }
    return render(req, "3_muallif.html", d)



def k_soni(req):
    d={
        "kitoblar": Kitob.objects.filter(muallif__Kitoblar_soni__lt=10)
    }
    return render(req, "kitob.html", d)


def biron_id(r, pk):
    d={
        "records": Record.objects.get(id=pk)
    }
    return render(r, "bironta_record.html", d)

def bitiruvchi_t_r(r):
    d={
        "recordslar": Record.objects.filter(talaba__kurs=4)
    }
    return render(r, "bironta_record.html", d)


#Ma'lumotni o'chirish va uni qidirish

def talaba_ochir(rec, pk):
    Talaba.objects.get(id=pk).delete()
    return redirect("/students/")


def kitob_ochirish(rec, pk):
    Kitob.objects.get(id=pk).delete()
    return redirect("/kitob/")
