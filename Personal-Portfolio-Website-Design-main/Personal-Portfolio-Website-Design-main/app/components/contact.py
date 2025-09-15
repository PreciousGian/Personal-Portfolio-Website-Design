import reflex as rx


def social_link(icon_tag: str, url: str, name: str) -> rx.Component:
    """A link to a social media profile."""
    return rx.el.a(
        rx.icon(
            tag=icon_tag,
            class_name="h-6 w-6 text-slate-500 dark:text-slate-400 group-hover:text-sky-500 transition-colors",
        ),
        rx.el.span(
            name,
            class_name="ml-3 text-slate-700 dark:text-slate-300 group-hover:text-sky-500 transition-colors",
        ),
        href=url,
        is_external=True,
        class_name="group flex items-center p-3 bg-slate-100 dark:bg-slate-800/50 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-800 transition-colors",
    )


def contact_section() -> rx.Component:
    """The contact section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Get in Touch",
                class_name="text-3xl font-bold tracking-tighter sm:text-4xl text-center",
            ),
            rx.el.p(
                "Feel free to connect with me on my professional networks.",
                class_name="mx-auto max-w-[600px] text-slate-500 md:text-lg dark:text-slate-400 mt-4 text-center",
            ),
            rx.el.div(
                social_link(
                    "linkedin",
                    "https://www.linkedin.com/in/keitumetseplefaso",
                    "LinkedIn",
                ),
                social_link("github", "https://github.com/PreciousGian", "GitHub"),
                class_name="mt-8 grid grid-cols-1 sm:grid-cols-2 max-w-sm mx-auto gap-4",
            ),
            class_name="container px-4 md:px-6",
        ),
        id="contact",
        class_name="w-full py-12 md:py-24 lg:py-32 bg-slate-100 dark:bg-slate-900/50",
    )