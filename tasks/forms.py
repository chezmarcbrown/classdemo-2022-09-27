from django import forms
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    slug = forms.SlugField(label="URLish")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=3)