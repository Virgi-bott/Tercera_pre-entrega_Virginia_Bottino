from django import forms

class KayakistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField()
    ubicacion = forms.CharField(max_length=40)
    club = forms.CharField()

class ClubFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField()
    localidad = forms.CharField(max_length=40)
    provincia = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    
class TravesiaFormulario(forms.Form):
    kayakista = forms.CharField(max_length=40, widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    email = forms.EmailField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    partida = forms.CharField(max_length=40, widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    distancia = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    fecha = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))


class BuscarDatoForm(forms.Form):
    nombre = forms.CharField(max_length=40)