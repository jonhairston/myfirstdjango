__author__ = 'Jon'
from django.core.serializers import json
from django.utils import simplejson # seprecated
from tastypie.serializers import Serializer

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from polls.models import Poll


class PrettyJSONSerialer(Serializer):
    json_indent = 4

    def to_jsonp(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent)

class PollResource(ModelResource):
    choicez= fields.ToManyField('polls.api.ChoiceResource', 'choices', related_name='poll', full=True)
    class Meta:
        queryset = Poll.objects.all()
        serializer = PrettyJSONSerialer()
        authorization = Authorization()


class ChoiceResource(ModelResource):
    poll = fields.ForeignKey('polls.api.PollResource', 'poll',related_name='choicez')

    class Meta:
        queryset = Poll.objects.all()
        serializer = PrettyJSONSerialer()
        authorization = Authorization()
