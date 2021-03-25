from django import template
from django.contrib.contenttypes.models import ContentType

from ratings.forms import RatingForm
from ratings.models import Rating

register = template.Library()

@register.inclusion_tag('ratings/rating.html', takes_context=True)
def rating(context, *args, **kwargs):
    '''
    {% load rating %}
    {% rating %}
    '''
    obj = kwargs.get("object")
    rating_only = kwargs.get("rating_only")
    request = context['request']
    user = None
    if request.user.is_authenticated:
        user = request.user
    app_label = obj._meta.app_label # playlists
    model_name = obj._meta.model_name
    if app_label == "playlists":
        if model_name == 'movieproxy' or 'tvshowproxy':
            model_name = 'playlist'
    c_type = ContentType.objects.get(app_label=app_label,model=model_name)
    avg_rating = Rating.objects.filter(content_type=c_type, object_id=obj.id).rating()
    context = {
        'value': avg_rating,
        'form': None
    }

    display_form = False
    if user is not None:
        display_form = True
    if rating_only is True:
        display_form = False
    if display_form:
        context['form'] = RatingForm(initial={
            "object_id": obj.id,
            "content_type_id": c_type.id,
            "next": request.path,
        })
    return context