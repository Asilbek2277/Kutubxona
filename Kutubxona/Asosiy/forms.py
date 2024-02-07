from django import forms
from .models import *

class TalabaForm(forms.Form):
    ism=forms.CharField(label='Ism')
    kurs=forms.IntegerField(label='Kurs')
    kitob_soni=forms.IntegerField(label='Kitob soni')


class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields= '__all__'


#1-misol
class MuallifForm(forms.ModelForm):
    class Meta:
        model=Muallif
        fields='__all__'


#2-misol
class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields='__all__'

#3-misol
class KutubxonachiForm(forms.ModelForm):
    class Meta:
        model=Kutubxonachi
        fields='__all__'
