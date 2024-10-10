# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Widgets for WakeUp."""

from gi.repository import Adw, Gtk


@Gtk.Template(resource_path="/de/swsnr/wakeup/ui/wakeup-application-window.ui")  # pyright: ignore[reportUntypedClassDecorator]
class WakeUpApplicationWindow(Adw.ApplicationWindow):
    """The main application window."""

    __gtype_name__ = "WakeUpApplicationWindow"
