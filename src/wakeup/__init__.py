# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


"""GNOME application to wake up devices in networks using WakeOnLan."""

import sys

import gi

gi.require_version("Adw", "1")
gi.require_version("Gtk", "4.0")


APP_ID = "de.swsnr.wakeup"


def set_default_icon_name(_app: object) -> None:
    """Set the default icon name after startup."""
    from gi.repository import Gtk

    Gtk.Window.set_default_icon_name(APP_ID)


def register_resources() -> None:
    """Load and register Gio resources."""
    import pkgutil

    from gi.repository import Gio, GLib

    # TODO: Compile resource bundle with uv?
    data = pkgutil.get_data("wakeup", "wakeup.gresource")
    if not data:
        raise LookupError("Resource data not found")  # noqa: TRY003
    Gio.resources_register(Gio.Resource.new_from_data(GLib.Bytes.new(data)))


def main() -> int:
    """Entry point for wakeup."""
    import logging

    from gi.repository import GLib

    # TODO: Make logging configurable, and hook up glib logging?
    logging.basicConfig(level=logging.INFO)

    # Register resources before importing any widgets, otherwise Gtk.Template
    # doesn't find our resources.
    register_resources()

    from wakeup.application import WakeUpApplication

    app = WakeUpApplication(application_id=APP_ID)
    app.connect("startup", set_default_icon_name)
    GLib.set_application_name("WakeUp")

    return app.run(sys.argv)
