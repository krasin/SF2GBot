#!/usr/bin/env python
#
# Copyright 201 Pavel Krasilnikov (p.krasilnikov@gmail.com).

import logging, email
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app

class SF2GMailHandler(InboundMailHandler):
	def receive(self, mail_message):
		logging.info("Received a message from: " + mail_message.sender)
		logging.info("Message's subject: " + mail_message.subject)

application = webapp.WSGIApplication([SF2GMailHandler.mapping()], debug=True)

def main():
	logging.info("in the email!")   
	run_wsgi_app(application)

if __name__ == '__main__':
    main()
