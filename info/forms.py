from django import forms
from django.utils import timezone

def default_start():
    return timezone.now() - timezone.timedelta(days=30)

def default_end():
    return timezone.now()


class SearchForm(forms.Form):
    SEARCH_OPTION_CHOICES = [
        ('ON', '주문번호'),
        ('GM', '상품명')
    ]
    search_option = forms.ChoiceField(
        choices=SEARCH_OPTION_CHOICES)
    search_keyword = forms.CharField(max_length=100, required=False)
    start_date = forms.DateField(initial=default_start)
    end_date = forms.DateField(initial=default_end)
