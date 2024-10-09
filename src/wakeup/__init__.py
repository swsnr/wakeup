# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


"""GNOME application to wake up devices in networks using WakeOnLan."""


def say_hello(name: str) -> None:
    """Test type errors."""
    print(f"Hello {name}")


def main() -> None:
    """Entry point for wakeup."""
    say_hello("wakeup")
