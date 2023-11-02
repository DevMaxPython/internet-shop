from django import forms
from .models import Comments, DeliveriInformation


class CommentForm(forms.ModelForm):
    comment_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Comments
        fields = ('comment',)


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)


class DeliveryRegistrationForm(forms.ModelForm):
    basket_items = forms.TextInput()
    class Meta:
        model = DeliveriInformation
        fields = ['city', 'street', 'numder_of_house', 'phone', 'basket_information', 'choose_payment_method']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'field_input'}), 
            'street': forms.TextInput(attrs={'class': 'field_input'}), 
            'numder_of_house': forms.NumberInput(attrs={'class': 'field_input'}), 
            'phone': forms.TextInput(attrs={'class': 'field_input'}),
            'choose_payment_method': forms.Select(attrs={'class': 'payment_method_field'})
        }