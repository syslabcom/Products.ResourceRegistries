from Acquisition import aq_inner
from Products.PythonScripts.standard import url_quote
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName


registries = (
    'portal_css',
    'portal_javascripts',
    'portal_kss',
    )


class authOnlyJSON(BrowserView):
    """ List auth-only registry resources. """

    def __call__(self):
        context = aq_inner(self.context)
        skinname = url_quote(context.getCurrentSkinName())

        result = []
        for registry_name in registries:
            registry = getToolByName(context, registry_name)
            registry_url = registry.absolute_url()
            resources = registry.getAuthOnlyResources(context)
            for resource in resources:
                try:
                    inline = bool(resource.getInline())
                except AttributeError:
                    inline = False
                if not inline:
                    if resource.isExternalResource():
                        src = '"%s"' % (resource.getId(),)
                    else:
                        src = '"%s/%s/%s"' % (registry_url, skinname, resource.getId())
                    result.append(src)

        return "{items:[%s]}" % ",".join(result)
