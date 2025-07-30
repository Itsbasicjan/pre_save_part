# plugins/remove_empty_link.py

from plugin import InvenTreePlugin
from part.models import Part

class RemoveEmptyLinkPlugin(InvenTreePlugin):
    NAME = "RemoveEmptyLinkPlugin"
    DESCRIPTION = "Entfernt leere 'link'-Felder beim Speichern von Parts"

    def pre_save_part(self, sender, instance: Part, data: dict, user, **kwargs):
        # Falls 'link' ein leerer String ist, entfernen
        if data.get('link', '').strip() == "":
            data.pop('link')
