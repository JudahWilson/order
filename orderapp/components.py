'''
Reusable UI components
Documentation at https://github.com/Xzya/django-web-components
'''
from django_web_components import component

@component.register("Card")
class Card(component.Component):
    template_name = "components/card.html"
    
    
@component.register("Navbar")
class Navbar(component.Component):
    template_name = "components/navbar.html"
    
    
@component.register("TicketView")
class Navbar(component.Component):
    template_name = "components/ticketview.html"
    
    
@component.register("TicketEdit")
class Navbar(component.Component):
    template_name = "components/ticketedit.html"