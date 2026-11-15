"""Libadwaita appearance honors system/portal and high-contrast settings."""
from gi.repository import Adw, Gdk, Gtk


APP_CSS = """
/* Surfaces: use native theme colors so light, dark and high-contrast modes work. */
.card {
    border-radius: 12px;
}

.metric-card {
    min-height: 112px;
    padding-top: 4px;
    padding-bottom: 4px;
}

.metric-card .title-2 {
    font-weight: 700;
}

.boxed-list > row {
    padding: 4px 6px;
}

.page-title {
    margin-bottom: 2px;
}

.page-subtitle {
    line-height: 1.35;
}

.mono-value {
    font-family: monospace;
}

.status-ok {
    color: @success_color;
}

.status-warning {
    color: @warning_color;
}

.status-error {
    color: @error_color;
}
"""


class ThemeController:
    def __init__(self):
        self.mode = "system"
        self.manager = Adw.StyleManager.get_default()
        self.provider = Gtk.CssProvider()
        self.provider.load_from_data(APP_CSS.encode("utf-8"))
        self.display = Gdk.Display.get_default()
        if self.display:
            Gtk.StyleContext.add_provider_for_display(
                self.display,
                self.provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
            )

    def apply(self, theme):
        self.mode = theme
        self.manager.set_color_scheme(
            {
                "system": Adw.ColorScheme.DEFAULT,
                "light": Adw.ColorScheme.FORCE_LIGHT,
                "dark": Adw.ColorScheme.FORCE_DARK,
            }[theme]
        )

    def cleanup(self):
        if self.display:
            Gtk.StyleContext.remove_provider_for_display(self.display, self.provider)
            self.display = None
