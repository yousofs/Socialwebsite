from django import forms

message = {
    'required': 'این فیلد الزامی است',
    'invalid': 'لطفا یک ایمیل معتبر وارد کنید',
    'max_length': 'تعداد کاراکتر ها بیشتر از حد مجاز است',
    'min_length': 'حداقل ۸ کاراکتر لازم است',
}


class UserLoginForm(forms.Form):
    username = forms.CharField(error_messages=message,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
    password = forms.CharField(error_messages=message,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(error_messages=message, max_length=30, min_length=8,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
    email = forms.EmailField(error_messages=message, max_length=50,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(error_messages=message, max_length=40, min_length=8,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
