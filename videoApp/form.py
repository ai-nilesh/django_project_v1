from django import forms


# this is the user form where user submit the request
class UserForm(forms.Form):
    inp_title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'usertitle',
        'id': 'user_title',
        'placeholder': 'Video title'
    }))

    inp_desc = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'text',
        'name': 'userdesc',
        'id': 'user_desc',
        'placeholder': 'Video desc'

    })

    )
