"""Shared GTK4 page primitives."""
from __future__ import annotations

from gi.repository import Gtk


class BasePage(Gtk.Box):
    def __init__(self, title: str, subtitle: str = "") -> None:
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.add_css_class("workspace-page")
        self.set_margin_top(28)
        self.set_margin_bottom(28)
        self.set_margin_start(28)
        self.set_margin_end(28)
        heading = Gtk.Label(label=title, xalign=0)
        heading.add_css_class("title-1")
        heading.add_css_class("page-title")
        self.append(heading)
        if subtitle:
            label = Gtk.Label(label=subtitle, xalign=0, wrap=True)
            label.add_css_class("dim-label")
            label.add_css_class("page-subtitle")
            self.append(label)

    def cleanup(self) -> None:
        """Release page-owned subscriptions, timers, and background hooks."""
        return None


def section(title: str, child: Gtk.Widget) -> Gtk.Box:
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    heading = Gtk.Label(label=title, xalign=0)
    heading.add_css_class("heading")
    box.append(heading)
    box.append(child)
    return box
