# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""The WakeUp application."""

import logging
from typing import override

from gi.repository import Adw, Gio, GLib

from wakeup.widgets import WakeUpApplicationWindow

LOG = logging.getLogger(__name__)


class WakeUpApplication(Adw.Application):
    """The application object for WakeUp."""

    def _activate_quit(
        self, _act: Gio.SimpleAction, _param: GLib.Variant | None
    ) -> None:
        """Quit the application."""
        self.quit()

    def _activate_about(
        self, _act: Gio.SimpleAction, _param: GLib.Variant | None
    ) -> None:
        """Show an about dialog for the application."""
        dialog = Adw.AboutDialog.new_from_appdata(
            "/de/swsnr/wakeup/de.swsnr.wakeup.metainfo.xml",
            # TODO: Version!
        )
        dialog.present(self.get_active_window())

    def _create_actions(self) -> list[Gio.Action]:
        """Create actions for the application."""
        quit = Gio.SimpleAction.new("quit")
        quit.connect("activate", self._activate_quit)
        about = Gio.SimpleAction.new("about")
        about.connect("activate", self._activate_about)
        return [quit, about]

    @override
    def do_startup(self) -> None:
        """Handle application startup."""
        Adw.Application.do_startup(self)
        LOG.info("Starting application")

        for action in self._create_actions():
            self.add_action(action)

        self.set_accels_for_action("win.add_device", ["<Control>n"])
        self.set_accels_for_action("window.close", ["<Control>w"])
        self.set_accels_for_action("app.quit", ["<Control>q"])

        # TODO: Load devices

    @override
    def do_activate(self) -> None:
        """Activate the application."""
        window = self.get_active_window()
        if not window:
            window = WakeUpApplicationWindow(application=self)
        window.present()
