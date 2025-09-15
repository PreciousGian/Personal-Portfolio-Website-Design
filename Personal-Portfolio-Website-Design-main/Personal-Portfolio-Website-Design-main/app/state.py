import reflex as rx
from typing import Literal


class PortfolioState(rx.State):
    """The app state."""

    theme: Literal["light", "dark"] = "dark"

    @rx.event
    def toggle_theme(self):
        """Toggle the theme between light and dark."""
        self.theme = "light" if self.theme == "dark" else "dark"

    @rx.var
    def theme_class(self) -> str:
        """Return the theme class."""
        return "dark" if self.theme == "dark" else ""

    @rx.var
    def icon_color(self) -> str:
        """Return the icon color based on the theme."""
        return "#FFFFFF" if self.theme == "dark" else "#0F172A"