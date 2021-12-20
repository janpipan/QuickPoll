from django.forms import ModelForm, TextInput, CharField, Textarea
from django.forms.models import inlineformset_factory

from .models import Answer, Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'multiple_answers','add_answer']
        
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        labels = {
            'answer' : '',
        }
        widgets = {
            'answer' : TextInput(attrs={'placeholder' : 'Answer'})
        }


