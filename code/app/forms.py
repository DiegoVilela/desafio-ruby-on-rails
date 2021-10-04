from django import forms


class UploadFileForm(forms.Form):
    finance_file = forms.FileField()
