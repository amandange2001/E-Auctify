from e_auctionapp.models import Product
from django.forms import ModelForm


class AuctionForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['userid']

from django import forms
from .models import Bid

class BidForm(forms.Form):
    bid_amount = forms.DecimalField(label='Your Bid', min_value=0)

    def __init__(self, product_base_price, *args, **kwargs):
        super(BidForm, self).__init__(*args, **kwargs)
        self.product_base_price = product_base_price

    def clean_bid_amount(self):
        bid_amount = self.cleaned_data['bid_amount']

        # Additional validation for bid amount
        if Bid.objects.filter(product=self.product_base_price).exists():
            if bid_amount <= Bid.objects.filter(product=self.product_base_price).latest('timestamp').amount:
                raise forms.ValidationError("Bid amount must be greater than the previous bid.")
        elif bid_amount <= self.product_base_price:
            raise forms.ValidationError("The first bid must be greater than the base price.")

        return bid_amount
