import reflex as rx
import datetime


def footer() -> rx.Component:
    """The footer component."""
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                f"© {datetime.date.today().year} Keitumetse Lefaso. All rights reserved.",
                class_name="text-sm text-slate-500 dark:text-slate-400",
            ),
            class_name="container mx-auto flex h-14 items-center justify-center px-4 md:px-6",
        ),
        class_name="border-t border-slate-200 dark:border-slate-800",
    )