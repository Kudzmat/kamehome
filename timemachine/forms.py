from django import forms


class CharacterForm(forms.Form):
    choice = forms.ChoiceField(label='Mission', choices=[('', '--Select an option --'),
                                                         ('Something light hearted', 'Something light hearted'),
                                                         ('A little danger', 'A little danger'),
                                                         ])
