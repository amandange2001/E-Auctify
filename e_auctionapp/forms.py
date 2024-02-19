from e_auctionapp.models import Product
from django.forms import ModelForm


class AuctionForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['userid']
