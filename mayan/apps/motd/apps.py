from __future__ import unicode_literals

import logging

from django.utils.translation import ugettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.acls.links import link_acl_list
from mayan.apps.acls.permissions import permission_acl_edit, permission_acl_view
from mayan.apps.common.apps import MayanAppConfig
from mayan.apps.common.menus import menu_object, menu_secondary, menu_setup
from mayan.apps.navigation import SourceColumn

from .links import (
    link_message_create, link_message_delete, link_message_edit,
    link_message_list
)
from .permissions import (
    permission_message_delete, permission_message_edit,
    permission_message_view
)

logger = logging.getLogger(__name__)


class MOTDApp(MayanAppConfig):
    app_namespace = 'motd'
    app_url = 'messages'
    has_rest_api = True
    has_tests = True
    name = 'mayan.apps.motd'
    verbose_name = _('Message of the day')

    def ready(self):
        super(MOTDApp, self).ready()

        Message = self.get_model('Message')
        ModelPermission.register(
            model=Message, permissions=(
                permission_acl_edit, permission_acl_view,
                permission_message_delete, permission_message_edit,
                permission_message_view
            )
        )
        SourceColumn(
            source=Message, label=_('Enabled'), attribute='enabled'
        )
        SourceColumn(
            source=Message, label=_('Start date time'),
            func=lambda context: context['object'].start_datetime or _('None')
        )
        SourceColumn(
            source=Message, label=_('End date time'),
            func=lambda context: context['object'].end_datetime or _('None')
        )

        menu_object.bind_links(
            links=(
                link_message_edit, link_acl_list, link_message_delete
            ), sources=(Message,)
        )
        menu_secondary.bind_links(
            links=(link_message_create,),
            sources=(Message, 'motd:message_list', 'motd:message_create')
        )
        menu_setup.bind_links(
            links=(link_message_list,)
        )
