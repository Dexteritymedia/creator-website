from django import template

from app.models import *

register = template.Library()

def creator_contents(context):
    form = contact_view(request)
    content = Content.objects.all()
    faqs = FAQ.objects.all()
    works = WorkHistory.objects.filter(accept=True)
    try:
        creator_detail = CreatorDetail.objects.get()
    except ObjectDoesNotExist:
        creator_detail = None
    context = {
        'form': form,
        'content': creator_detail,
        'creator_contents': content,
        'faqs': faqs,
        'works': works,
    }
    return context


@register.simple_tag
def current_title():
    return 'Title'
