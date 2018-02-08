from django import forms


class WorksheetForm(forms.Form):
    class Meta:
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }

    problem_count = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), min_value=2, max_value=50)
    min_val = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), min_value=-1000, max_value=1000)
    max_val = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), min_value=-1000, max_value=1000)
    qr = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'custom-control-input'}))

    def clean(self):
        cleaned_data = super().clean()
        min_val = cleaned_data.get('min_val')
        max_val = cleaned_data.get('max_val')
        if min_val and max_val:
            if min_val > max_val:
                raise forms.ValidationError(
                    "The minimum value can not be higher than the maximum value."
                )