from django import forms
from  .models import Resume 

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume 
        fields =  ['id','name','dob','gender','locality','city','pin','state','mobile','Current_city','Profile_image','myfile']
        labels ={'name':'Full Name', 'dob':'Date of Birth','pin':'Pin Code','mobile':'Contact No.','email':'Email ID','profile_image':'Profile Image','myfile':'Document'}
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-select'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-select'}),
            'Current_city': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'Prefered_Job_City': forms.Select(attrs={'class':'form-select'}),  
            
        }