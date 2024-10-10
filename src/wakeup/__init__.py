# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


"""GNOME application to wake up devices in networks using WakeOnLan."""

import sys
from typing import override

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import GLib, Gtk  # noqa: E402


class MyApplication(Gtk.Application):
    """Dummy application to test building and running pygobject apps."""

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__(application_id="com.example.MyGtkApplication")
        GLib.set_application_name("My Gtk Application")

    @override
    def do_activate(self) -> None:
        """Handle application activation."""
        window = Gtk.ApplicationWindow(application=self, title="Hello World")
        window.present()


def main() -> int:
    """Entry point for wakeup."""
    app = MyApplication()
    return app.run(sys.argv)
