from plugin import InvenTreePlugin
from part.models import Part

class RemoveEmptyLinkPlugin(InvenTreePlugin):
    NAME = "RemoveEmptyLinkPlugin"
    SLUG = "remove-empty-link"
    TITLE = "Leere Links entfernen"
    VERSION = "1.0"
    DESCRIPTION = "Plugin entfernt leere Strings im Feld 'link', um Fehler zu verhindern."

    def pre_save_part(self, sender, instance: Part, data: dict, user, **kwargs):
        if data.get("link", "").strip() == "":
            data.pop("link")
