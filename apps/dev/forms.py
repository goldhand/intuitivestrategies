from django.utils.translation import gettext_lazy as _ 
from django import forms
from settings import PROJECT_ROOT



def fontfamilies():
        f = open(PROJECT_ROOT + '/apps/dev/fontfamilies.py', 'r')
        famList = f.read()
        famList = famList.split(';\nfont-family: ')
        famList[0] = famList[0][13:]
        famList[-1] = famList[-1][:-2]
	famList_tuples = []
	for item in famList:
		x = item.split(', ')
		xdisplay = x[0].strip("'")
		famList_tuples.append((item, xdisplay))
        return famList_tuples

font_family_choices = fontfamilies()

class EditStyle(forms.Form):
	font_family = forms.ChoiceField(choices=font_family_choices)
	font_size = forms.CharField(max_length=3)
	font_color = forms.CharField(max_length=6)
