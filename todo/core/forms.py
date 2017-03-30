from django import forms
from django.core.exceptions import ValidationError


class TitleWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        return """
            <label for="{field_id}" style="color: red">{name}</label>
            <input id="{field_id}" maxlength="5" name="title" type="text" required="" value="{value}">
        """.format(
            field_id=attrs.get('id'),
            name=name,
            value=value or ''
        )


class TestForm(forms.Form):
    title = forms.CharField(max_length=5, widget=TitleWidget)
    text = forms.CharField(max_length=255)

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if 'a' in title:
            raise ValidationError('a not permitted')
        return title
