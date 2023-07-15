from .models import CapsuleGram


# form for uploading pictures to Capsule Gram
class CapsuleGramForm(forms.ModelForm):
    class Meta:
        model = CapsuleGram
        fields = ['gram_image']
