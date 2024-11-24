from django import forms

from .models import Category, Contact, WorkHistory

class BudgetForm(forms.Form):
    budget = forms.DecimalField(label="Enter your budget", max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={"placeholder":"e.g., 20000", "class":"input input-bordered w-full"}))
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all().exclude(name='Stay'), widget=forms.CheckboxSelectMultiple())
    include_accommodation = forms.BooleanField(required=False, label="Include Accommodation", widget=forms.CheckboxInput())


class ContactForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"your@email.com", "class":"input input-bordered w-full"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"textarea textarea-bordered h-24", "placeholder":"Your message", "id":"floatingTextarea"}))
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'phone_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'input input-bordered w-full', "placeholder":"Your name"})
        self.fields['phone_no'].widget.attrs.update({'class':'input input-bordered w-full', "placeholder":"Enter your phone number"})

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_no = cleaned_data.get('phone_no')

        if not email and not phone_no:
            raise forms.ValidationError("Please enter either your email or phone number")



class WorkHistoryForm(forms.ModelForm):
    class Meta:
        model = WorkHistory
        exclude = ['accept']



