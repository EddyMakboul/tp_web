from django import forms

class SaisieChansonForm(forms.Form):
    groupe = forms.CharField(label='Groupe*', max_length=30)
    titre = forms.CharField(label='Titre*', max_length=50)
    youtube=forms.CharField(label='Youtube',max_length=100,required=False)
    paroles=forms.CharField(
        label="Paroles",
        widget=forms.Textarea(
            attrs={'cols':'90','rows':'10','class':'saisie-paroles'}),
        required=False)
