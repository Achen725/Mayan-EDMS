from django.utils.translation import ugettext_lazy as _

from mayan.apps.dynamic_search.classes import SearchModel

from .permissions import permission_tag_view

tag_search = SearchModel(
    app_label='tags', model_name='Tag',
    permission=permission_tag_view,
    serializer_path='mayan.apps.tags.serializers.TagSerializer'
)

tag_search.add_model_field(
    field='label', label=_('Label')
)

tag_search.add_model_field(
    field='color', label=_('Color')
)
