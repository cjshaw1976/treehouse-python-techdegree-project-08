from django import template
from django.db.models import Count

from minerals.models import Mineral

register = template.Library()


# All letters
@register.inclusion_tag('letter_list.html', takes_context=True)
def all_letters(context):
    return {'path': context['request'].path[1:-1]}


# Gets all groups
@register.inclusion_tag('group_list.html', takes_context=True)
def all_groups(context):
    groups = (Mineral.objects.values('group')
              .annotate(Count('id')).order_by('group'))
    return {'groups': groups, 'path': context['request'].path[1:-1]}


# Gets all categories
@register.inclusion_tag('category_list.html', takes_context=True)
def all_categories(context):
    categories = (Mineral.objects.values('category')
                  .annotate(Count('id')).order_by('category'))
    return {'categories': categories, 'path': context['request'].path[1:-1]}
