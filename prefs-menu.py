from gi.repository import GObject, Gtk, Gedit

UI_XML = """<ui>
<menubar name="MenuBar">
    <menu name="EditMenu" action="Edit">
      <placeholder name="EditPreferencesMenuHolder">
        <menuitem name="EditPreferencesMenu" action="EditPreferences"/>
      </placeholder>
    </menu>
</menubar>
</ui>"""

class ExtensionPrefsMenu(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "ExtensionPrefsMenu"
    window = GObject.property(type=Gedit.Window)
   
    def __init__(self):
        GObject.Object.__init__(self)
    
    def _add_ui(self):
        manager = self.window.get_ui_manager()
	# We don't need to create a new action here, as GEdit
	# already provides the EditPreferences action. We're
	# simply binding it to the menu item.
        self._ui_merge_id = manager.add_ui_from_string(UI_XML)
        manager.ensure_update()
        
    def do_activate(self):
        self._add_ui()

    def do_deactivate(self):
        self._remove_ui()

    def do_update_state(self):
        pass
    
    def _remove_ui(self):
        manager = self.window.get_ui_manager()
        manager.remove_ui(self._ui_merge_id)
        manager.ensure_update()
