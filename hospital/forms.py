from django import forms 

class RegisterForm(forms.Form) :
    username = forms.CharField(min_length=3 , max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput , min_length=5)
    confirm_password = forms.CharField(widget=forms.PasswordInput , min_length=5)

    def clean_username(self):
        username = self.cleaned_data["username"]

        if " " in username :
            raise forms.ValidationError("username cannot contain space")

        return username

    def clean(self):
        cleaned_data = super().clean() 

        password = cleaned_data.get("password")

        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password :
            raise forms.ValidationError("passwords are not same") 