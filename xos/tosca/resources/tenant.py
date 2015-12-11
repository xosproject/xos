import os
import pdb
import sys
import tempfile
sys.path.append("/opt/tosca")
from translator.toscalib.tosca_template import ToscaTemplate
import pdb

from ceilometer.models import Tenant, Service

from xosresource import XOSResource

class XOSTenant(XOSResource):
    provides = "tosca.nodes.Tenant"
    xos_model = Tenant
    name_field = None
    copyin_props = ("kind", "service_specific_attribute")

    def get_xos_args(self, throw_exception=True):
        args = super(XOSTenant, self).get_xos_args()

        provider_name = self.get_requirement("tosca.relationships.MemberOfService", throw_exception=throw_exception)
        if provider_name:
            args["provider_service"] = self.get_xos_object(Service, throw_exception=throw_exception, name=provider_name)

        return args

    def get_existing_objs(self):
        args = self.get_xos_args(throw_exception=False)
        provider_service = args.get("provider", None)
        if provider_service:
            return [ self.get_xos_object(provider_service=provider_service) ]
        return []

    def postprocess(self, obj):
        pass

    def can_delete(self, obj):
        return super(XOSTenant, self).can_delete(obj)
