from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag("blog/BLBL/NAV/navbar.html")
def navbar_category():
    return {
        "category": Category.objects.all()
    }
