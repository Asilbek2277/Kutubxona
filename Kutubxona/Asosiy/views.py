from django.shortcuts import render, redirect

from .models import *

from .forms import *

def all_books(request):
    if request.method == "POST":

        d=KitobForm(request.POST)
        if d.is_valid():
            d.save()



        # Kitob.objects.create(
        #     nom=request.POST.get("nomi"),
        #     janr=request.POST.get("janr"),
        #     sahifa=request.POST.get("sahifa"),
        #     muallif=Muallif.objects.get(id=request.POST.get("mualliflar")),
        # )
        return redirect("/books/")
    data = {
        "mualliflar": Muallif.objects.all(),
        "books": Kitob.objects.all(),
        "form": KitobForm()
    }
    return render(request, 'kitoblar.html', data)


def all_students(request):
    if request.method == "POST":

        d=TalabaForm(request.POST)
        if d.is_valid():
            Talaba.objects.create(
                ism=d.cleaned_data['ism'],
                kurs=d.cleaned_data['kurs'],
                kitob_soni=d.cleaned_data['kitob_soni']
            )




        # Talaba.objects.create(
        #     ism=request.POST.get("ismi"),
        #     kurs=request.POST.get("k"),
        #     kitob_soni=request.POST.get("k_soni"),
        # )
        # return redirect("/students/")

    natija = Talaba.objects.all()

    kiritilgan_ismi = request.GET.get("ismi")

    if kiritilgan_ismi is not None:
        natija = Talaba.objects.filter(ism__contains=kiritilgan_ismi)
    data = {
        "students": natija,
        'form': TalabaForm()
    }
    return render(request, "Students.html", data)


def bitiruvchilar(request):
    data = {
        "bitiruvchilar": Talaba.objects.filter(kurs=4)
    }
    return render(request, "Bitiruvchilar.html", data)


def talaba(request):
    data = {
        "bitiruvchilar": Talaba.objects.filter(kitob_soni__gt=0)
    }
    return render(request, "Bitiruvchilar.html", data)


def ism_a(request):
    data = {
        "bitiruvchilar": Talaba.objects.filter(ism__contains="a")
    }
    return render(request, "Bitiruvchilar.html", data)


def muallif(request):
    if request.method == "POST":
        if request.POST.get("tirikmi") == 'on':
            natija = True
        else:
            natija = False
        Muallif.objects.create(
            ism=request.POST.get("ismi"),
            jins=request.POST.get("jins"),
            tugilgan_sana=request.POST.get("date"),
            Kitoblar_soni=request.POST.get("kitob"),
            tirik=natija,
        )
        return redirect("/muallif/")
    data = {
        "mualliflar": Muallif.objects.all()
    }
    return render(request, "Mualliflar.html", data)


def muallif_ochirish(request, pk):
    Muallif.objects.get(id=pk).delete()
    return redirect("/muallif/")


def ikkinchi_talabalar(request):
    data = {
        "students": Talaba.objects.filter(kurs=2)
    }
    return render(request, "Students.html", data)


def bitta_talaba(request, pk):
    data = {
        "student": Talaba.objects.get(id=pk)
    }
    return render(request, "Bitta_talaba.html", data)


def hamma_mualliflar(request):

    if request.method=="POST":
        d = MuallifForm(request.POST)
        if d.is_valid():
            d.save()
            return redirect('/hamma_mualliflar/')

    natija = Muallif.objects.all()
    muallif_ismi = request.GET.get("muallif_ismi")
    if muallif_ismi is not None:
        natija = Muallif.objects.filter(ism__contains=muallif_ismi)
    data = {
        "mualliflar": natija,
        'form': MuallifForm()
    }
    return render(request, "Mualliflar.html", data)


def muallifni_tahrirlash(request, pk):
    if request.method == "POST":
        muallif = Muallif.objects.get(id=pk)
        muallif.ism = request.POST['ism']
        muallif.jins = request.POST['jins']
        muallif.tugilgan_sana = request.POST['sana']
        muallif.Kitoblar_soni = request.POST['kitoblar_soni']
        muallif.tirik = request.POST.get('tirikmi', False) == 'on'
        muallif.save()

        return redirect('/hamma_mualliflar/')

    context = {
        "muallif": Muallif.objects.get(id=pk)
    }

    return render(request, "Muallifni_tahrirlash.html", context)


def bitta_muallif(request, son):
    data = {
        "m": Muallif.objects.get(id=son)
    }
    return render(request, "Bitta_muallif.html", data)


def hamma_kitoblar(request):
    natija = Kitob.objects.all()

    kitob_nomi = request.GET.get("nomi")

    if kitob_nomi is not None:
        natija = Kitob.objects.filter(nom__contains=kitob_nomi)
    data = {
        "books": natija
    }
    return render(request, "kitoblar.html", data)


def bitta_kitob(request, pk):
    data = {
        "kitob": Kitob.objects.get(id=pk)
    }
    return render(request, "Bitta_kitob.html", data)




def recordlarni_tahrirlash(request, pk):
    if request.method == 'POST':
        record = Record.objects.get(id=pk)

        record.talaba=Talaba.objects.get(id=request.POST["ism"])

        record.Kitob=Kitob.objects.get(id=request.POST['kitob'])

        record.kutubxonachi=Kutubxonachi.objects.get(id=request.POST['kutubxonachi'])

       # record.olingan_sana=request.POST.get('olingan_sana')
        record.qaytardi=request.POST.get('qaytardi', False)=='on'
      #  record.qaytarish_sana=request.POST['qaytarish_sana']
        record.save()

        return redirect('/hamma_recordlar/')


    data={
        'recordlar': Record.objects.get(id=pk),
        'talabalar': Talaba.objects.all(),
        'kitoblar': Kitob.objects.all(),
        'kutubxonachilar':Kutubxonachi.objects.all()
    }

    return render(request, 'Recordlarni_tahrirlash.html', data)







def hamma_recordlar(request):
    # Recordlar jadvali uchun malumot qo'shish

    if request.method == 'POST':

        d=RecordForm(request.POST)
        if d.is_valid():
            d.save()


        # if request.POST.get("qaytardimi") == 'on':
        #     natija = True
        # else:
        #     natija = False
        #
        # Record.objects.create(
        #     talaba=Talaba.objects.get(id=request.POST.get('talaba')),
        #     Kitob=Kitob.objects.get(id=request.POST.get('kitob')),
        #     kutubxonachi=Kutubxonachi.objects.get(id=request.POST.get('k_chi')),
        #     olingan_sana=request.POST.get("sana"),
        #     qaytardi=natija,
        #     qaytarish_sana=request.POST.get("q_sana"),
        # )


        return redirect("/hamma_recordlar/")

    natija = Record.objects.all()
    kiritilgan_ism = request.GET.get("talaba_ismi")
    if kiritilgan_ism is not None:
        natija = Record.objects.filter(talaba__ism__contains=kiritilgan_ism)
    data = {
        "kitoblar": Kitob.objects.all(),
        "kutubxonachi": Kutubxonachi.objects.all(),
        "talabalar": Talaba.objects.all(),
        "record": natija,
        'form': RecordForm()
    }
    return render(request, "Records.html", data)


def recordni_ochirish(request, pk):
    Record.objects.get(id=pk).delete()
    return redirect("/hamma_recordlar/")


def tirik_mualliflar(request):
    data = {
        "mualliflar": Muallif.objects.filter(tirik=True)
    }
    return render(request, "Mualliflar.html", data)


kitoblar = Kitob.objects.order_by("-sahifa")


def uchta_kitob(req):
    d = {
        "kitob": kitoblar[0:3]
    }
    return render(req, "3kitob.html", d)


mualliflar = Muallif.objects.order_by("-Kitoblar_soni")


def uchta_muallif(req):
    d = {
        "muallif": mualliflar[0:3]
    }
    return render(req, "3_muallif.html", d)


recordlar = Record.objects.order_by("-olingan_sana")


def uchta_record(req):
    d = {
        "rec": recordlar[0:3]
    }
    return render(req, "3_record.html", d)


def t_m_kitoblari(r):
    d = {
        "kitoblar": Kitob.objects.filter(muallif__tirik=True)
    }
    return render(r, "trik_mualliflar_kitoblari.html", d)


def badiiy(r):
    d = {
        "kitoblar": Kitob.objects.filter(janr="Badiiy")
    }
    return render(r, "Badiiy_kitoblar.html", d)


yosh = Muallif.objects.order_by("tugilgan_sana")


def uchta_mu(req):
    d = {
        "muallif": yosh[0:3]
    }
    return render(req, "3_muallif.html", d)


def k_soni(req):
    d = {
        "kitoblar": Kitob.objects.filter(muallif__Kitoblar_soni__lt=10)
    }
    return render(req, "kitob.html", d)


def biron_id(r, pk):
    d = {
        "records": Record.objects.get(id=pk)
    }
    return render(r, "bironta_record.html", d)


def bitiruvchi_t_r(r):
    d = {
        "recordslar": Record.objects.filter(talaba__kurs=4)
    }
    return render(r, "bironta_record.html", d)


# Ma'lumotni o'chirish va uni qidirish

def talaba_ochir(rec, pk):
    Talaba.objects.get(id=pk).delete()
    return redirect("/students/")


def kitob_ochirish(rec, pk):
    Kitob.objects.get(id=pk).delete()
    return redirect("/kitob/")


def kutubxonachilarni_tahrirlash(request, pk):
    if request.method=='POST':
        kutubxonachi=Kutubxonachi.objects.get(id=pk)
        kutubxonachi.ism=request.POST['ism']
        kutubxonachi.ish_vaqti=request.POST['ish_vaqti']
        kutubxonachi.save()

        return redirect('/kutubxonachilar/')

    data={
        'kutubxonachilar': Kutubxonachi.objects.get(id=pk)

    }
    return render(request, 'Kutubxonachini_tahrirlash.html', data)


def kutubxonachilar(request):
    if request.method == 'POST':

        d=KutubxonachiForm(request.POST)

        if d.is_valid():
            d.save()

        # Kutubxonachi.objects.create(
        #     ism=request.POST.get("ismi"),
        #     ish_vaqti=request.POST.get("vaqt"),
        # )
        return redirect("/kutubxonachilar/")
    data = {
        "kutubxonachilar": Kutubxonachi.objects.all(),
        'forms': KutubxonachiForm()
    }
    return render(request, "Kutubxonachilar.html", data)


def talaba_tahrirla(request, pk):
    if request.method == "POST":
        talaba = Talaba.objects.get(id=pk)
        talaba.ism = request.POST["ism"]
        talaba.kurs = request.POST["kurs"]
        talaba.kitob_soni = request.POST["kitob_soni"]
        talaba.save()

        return redirect("/students/")

    context = {
        "talaba": Talaba.objects.get(id=pk)
    }
    return render(request, "talaba_tahrirla.html", context)
