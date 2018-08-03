from django.forms import ModelForm
from django import forms
from .models import Categoria, Reserva, ReservaRecurso, Recurso


class FormCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']


class FormReserva(ModelForm):
    class Meta:
        model = Reserva
        fields = ['statusReserva', 'dataReserva', 'horaReserva', 'observacoes']


class FormReservaRecurso(forms.Form, ModelForm):
    recurso = forms.ModelMultipleChoiceField(queryset=Recurso.objects.all())

    class Meta:
        model = ReservaRecurso
        fields = ['dataEmprestimo', 'horaEmprestimo', 'dataDevolucao', 'horaDevolucao', 'recurso']