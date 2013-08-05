gedit-prefs-menu
================

GEdit plugin to restore the Preferences option to the Edit menu.

This is especially useful when running gedit on a remote machine with
the display exported, since App Menu items are not exported to the
local display. (That's the reason I originally created the plugin.)

But, it's also good if you're just a creature of habit, and tend not to
reach for the App Menu in normal, window-centric activity.

`<rant>`
Especially since
GEdit still *has* a menu, and probably always will --- there was no reason
for Gnome to **remove** the Preferences option from the Edit menu!
`</rant>`

Installation
============

Simply place both the `.plugin` and `.py` files in your gedit plugins
directory (typically `$HOME/.local/share/gedit/plugins/`), and enable
"Preferences in Menu" from the Plugins list.
