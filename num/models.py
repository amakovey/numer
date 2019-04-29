from django.db import models
import re

class CustomField(models.TextField):
    def from_db_value(self, value, expression, connection, context):
        a=[]
        a=value.split(',')
        return a

    def get_db_prep_value(self, value, connection, prepared = True):
        if re.match(r'\d+(,\d+)?', value):
            return value
        else:
            pass

class SomeClass(models.Model):
    field = CustomField()
