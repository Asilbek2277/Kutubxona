from django.db import models

class Talaba(models.Model):
    ism=models.CharField(max_length=20)
    kurs=models.PositiveIntegerField()
    kitob_soni=models.PositiveIntegerField()

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    ism=models.CharField(max_length=20)
    jins=models.CharField(max_length=20, choices=[("Erkak", "Erkak"), ("Ayol", "Ayol")])
    tugilgan_sana=models.DateField()
    Kitoblar_soni=models.PositiveIntegerField()
    tirik=models.BooleanField()

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom=models.CharField(max_length=20)
    janr=models.CharField(max_length=20)
    sahifa=models.PositiveIntegerField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ism=models.CharField(max_length=20, null=True)
    ish_vaqti=models.CharField(max_length=50)

    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba=models.ForeignKey(Talaba, on_delete=models.CASCADE)
    Kitob=models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi=models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana=models.DateField()
    qaytardi=models.BooleanField(default=False)
    qaytarish_sana=models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.qaytarish_sana}"
