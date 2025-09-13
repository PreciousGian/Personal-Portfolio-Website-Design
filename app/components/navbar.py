import reflex as rx
from app.state import PortfolioState


def nav_link(text: str, section_id: str) -> rx.Component:
    """A navigation link that scrolls to a section."""
    return rx.el.a(
        text,
        on_click=rx.scroll_to(section_id),
        class_name="text-sm font-medium text-slate-400 hover:text-sky-400 transition-colors duration-200 cursor-pointer",
    )


def theme_toggle() -> rx.Component:
    """The theme toggle button."""
    return rx.el.button(
        rx.cond(
            PortfolioState.theme == "dark",
            rx.icon("sun", class_name="h-5 w-5 text-yellow-300"),
            rx.icon("moon", class_name="h-5 w-5 text-slate-700"),
        ),
        on_click=PortfolioState.toggle_theme,
        class_name="p-2 rounded-full bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 dark:hover:bg-slate-700 transition-colors duration-200",
    )


def navbar() -> rx.Component:
    """The navigation bar."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "KEITUMETSE PRECIOUS LEFASO",
                    class_name="text-lg font-bold text-slate-900 dark:text-white",
                ),
                class_name="flex items-center",
            ),
            rx.el.nav(
                nav_link("Home", "home"),
                nav_link("Education", "education"),
                nav_link("Hobbies", "hobbies"),
                nav_link("Contact", "contact"),
                class_name="hidden md:flex items-center gap-6",
            ),
            rx.el.div(theme_toggle(), class_name="flex items-center gap-4"),
            class_name="container mx-auto flex h-16 items-center justify-between px-4 md:px-6",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 bg-white/80 dark:bg-slate-950/80 backdrop-blur-sm border-b border-slate-200 dark:border-slate-800",
    )