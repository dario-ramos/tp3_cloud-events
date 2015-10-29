#!/usr/bin/env python

import environment
import webapp2
import model

class SelectEventController(webapp2.RequestHandler):
    def get(self):
        event_list = []
        allEventEntities = environment.MODEL.getEventRepository().getAll()
        for eventEntity in allEventEntities:
            event_list.append( eventEntity.name )
        template_values = {
            "title" : "Select event",
            "event_list" : event_list
        }
        template = environment.JINJA_ENVIRONMENT.get_template('select_event.html')
        self.response.write(template.render(template_values))