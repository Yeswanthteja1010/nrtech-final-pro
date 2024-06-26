from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def add_to_cart_url(slug, variation_id):
    return reverse('add-to-cart', kwargs={'slug': slug, 'variation_id': variation_id})

@register.simple_tag
def remove_from_cart_url(slug, variation_id):
    return reverse('remove-from-cart', kwargs={'slug': slug, 'variation_id': variation_id})

