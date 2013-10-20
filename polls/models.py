from django.db import models
import datetime
from django.utils import timezone


# Create your models here. Basically what do you need to represent the data correctly?
# answer that question here of course in models.py don't forget your imports above

# a model representation of Poll table data
class Poll(models.Model):
    # attributes of the model
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # returns the model in a human readable string in the admin panel and
    # in the template and anywhere else you need it in UTF-8 format
    def __unicode__(self):
        return self.question

    # creates a new table in the database called was_published recently
    # and gives it those attributes in the table and
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# a model representation of choice table data
class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

