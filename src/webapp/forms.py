from django import forms


class TaskForm(forms.Form):
    description = forms.CharField(label="Описание")
    deadline_date = forms.DateField(label="Дата")
    deadline_time = forms.TimeField(label="Время")
