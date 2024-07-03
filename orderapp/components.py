'''
Reusable UI components
Documentation at https://github.com/Xzya/django-web-components
'''
from django_web_components import component

@component.register("card")
class Card(component.Component):
    template_name = "components/card.html"
    
    
@component.register("navbar")
class Navbar(component.Component):
    template_name = "components/navbar.html"