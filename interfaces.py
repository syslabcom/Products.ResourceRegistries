from Interface import Interface


class IResourceRegistry(Interface):
    """A tool for registering and evaluating resource linkage."""

    def registerResource(id, expression='', enabled=1):
        """Register a resource."""

    def getEvaluatedResources(context):
        """Get the evaluated resource links and inline styles appropriate
        to the context for rendering.
        """

    def unregisterResource(id):
        """Unregister a registered resource."""

    def renameResource(old_id, new_id):
        """Change the id of a registered resource."""

    def moveResource(id, position):
        """Move a registered resource to the given position."""

    def getResourcePosition(id):
        """Get the position (order) of a resource given its id."""

    def moveResourceUp(id, steps=1, REQUEST=None):
        """Move the resource up 'steps' number of steps."""

    def moveResourceDown(id, steps=1, REQUEST=None):
        """Move the resource down 'steps' number of steps."""

    def moveResourceToTop(id, REQUEST=None):
        """Move the resource to the first position."""

    def moveResourceToBottom(id, REQUEST=None):
        """Move the resource to the last position."""

    def moveResourceBefore(id, dest_id, REQUEST=None):
        """Move the resource before the resource with dest_id."""

    def moveResourceAfter(id, dest_id, REQUEST=None):
        """Move the resource after the resource with dest_id."""

    def getResources():
        """Get the resource objects.

        For use in management screens.
        """


class ICSSRegistry(Interface):
    """A tool for registering and evaluating stylesheet linkage."""

    def registerStylesheet(id, expression='', media='', rel='stylesheet',
                           rendering='import', enabled=1):
        """Register a stylesheet."""

    def manage_addStylesheet(id, expression='', media='', rel='stylesheet',
                             rendering='import', enabled=True , REQUEST=None):
        """Add stylesheet from a ZMI form."""

    def manage_removeStylesheet(id, REQUEST=None):
        """Remove stylesheet from the ZMI."""

    def manage_saveStylesheets(REQUEST=None):
        """Save stylesheet data from form submission."""


class IJSRegistry(Interface):
    """A tool for registering and evaluating script linkage."""

    def registerScript(id, expression='', inline=False, enabled=True):
        """Register a script."""

    def manage_saveScripts(REQUEST=None):
        """Save script data from form submission."""

    def manage_addScript(id, expression='', inline=False, enabled=True , REQUEST=None):
        """Add script from a ZMI form."""

    def manage_removeScript(id, REQUEST=None):
        """Remove script via the ZMI."""
