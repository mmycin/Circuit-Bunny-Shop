from django import forms
from .models import Item

class SearchForm(forms.Form):
    query = forms.CharField(label="", max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'What are you looking for?', 'class': "search_box_text"}, ))


def formEvent(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query', '')
    if query:
        products = Item.objects.filter(Title__icontains=query)
    else:
        products = Item.objects.all()

    return form, query, products