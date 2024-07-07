from django import forms

class ListToDoClientForm(forms.form):
    title = forms.CharField(max_length=100)
    description = forms.TextField(blank=True)
    is_completed = forms.BooleanField(default=False)
    user = forms.ForeignKey(user, on_delete=forms.CASCADE)


