from django import forms 

class RedirectForm(forms.Form):
    PERIODS = [
        ("0", "0 Period"),
        ("1", "1 Period"),
        ("2", "2 Period"),
        ("3", "3 Period"),
        ("4", "4 Period"),
        ("5", "5 Period"),
        ("6", "6 Period"),
        ("7", "7 Period"),
        ("8", "8 Period"),
    ]

    select_period = forms.ChoiceField(choices=PERIODS)