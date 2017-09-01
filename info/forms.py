from django import forms
from django.utils import timezone

def default_start():
    return timezone.now() - timezone.timedelta(days=30)

def default_end():
    return timezone.now()


class SearchForm(forms.Form):
    # Follows esm convention
    SEARCH_OPTION_CHOICES = [
        ('','----'),
        # ('ON', '주문번호'), # Only supported for global search
        ('GN', '상품번호'),
        # ('GM', '상품명'), # Not supported for storefarm
        ('BN', '구매자이름'),
        ('BI', '구매자ID'),
        #('RCV', '수령인명') # Not supported for neworder stage
    ]
    from django.utils.safestring import mark_safe

    search_option = forms.ChoiceField(
        choices=SEARCH_OPTION_CHOICES, required=False)
    search_keyword = forms.CharField(max_length=100, required=False)
    start_date = forms.DateField(initial=default_start,
                                 widget = forms.SelectDateWidget())
    end_date = forms.DateField(initial=default_end,
                               widget = forms.SelectDateWidget())
