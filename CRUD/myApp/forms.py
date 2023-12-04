from django import forms
from .models import myRecords, userPics

class myForm(forms.ModelForm):
    class Meta:
        model=myRecords
        fields="__all__"
        widgets={
                "name":forms.TextInput(attrs={"class":"form-control","id":"floatingname","placeholder":"name"}),
                "email":forms.EmailInput(attrs={"class":"form-control","id":"floatingemail","placeholder":"email"}),
                "mobileNO":forms.TextInput(attrs={"class":"form-control","id":"floatingmobile","placeholder":"mobile"}),
                "city":forms.TextInput(attrs={"class":"form-control","id":"floatingcity","placeholder":"city"}),

            }
        
class picForm(forms.ModelForm):
    class Meta:
        model= userPics
        fields =['image']
        widgets = {'image':forms.FileInput(attrs={'class':'form-control','id':'formFile','accept':"*/image"})}