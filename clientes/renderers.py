#-*- coding: utf-8 -*-
import json
from rest_framework.renderers import JSONRenderer

class SujetoJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(SujetoJSONRenderer, self).render(data)
    
        return json.dumps({
            'sujetos': data
        })
