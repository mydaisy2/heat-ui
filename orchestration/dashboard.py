# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.utils.translation import ugettext_lazy as _

import horizon

class OrchestrationPanels(horizon.PanelGroup):
    name = _("Orchestration")
    slug = "orchestration"
    panels = ('stacks', 'task_flows', 'launch_stack',)

class Heat(horizon.Dashboard):
    name = _("Heat")
    slug = "heat"
    panels = (OrchestrationPanels,)
    default_panel = 'stacks'
    supports_tenants = True

horizon.register(Heat)