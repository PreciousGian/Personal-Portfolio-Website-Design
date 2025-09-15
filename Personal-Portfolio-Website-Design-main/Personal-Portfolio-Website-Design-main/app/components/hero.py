import reflex as rx


def hero_button(text: str, url: str, icon_tag: str) -> rx.Component:
    """A button for the hero section."""
    return rx.el.a(
        rx.el.button(
            rx.icon(tag=icon_tag, class_name="mr-2 h-4 w-4"),
            text,
            class_name="inline-flex items-center justify-center rounded-lg text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-background h-10 py-2 px-4 bg-slate-900 text-slate-50 hover:bg-slate-900/90 dark:bg-slate-50 dark:text-slate-900 dark:hover:bg-slate-50/90",
        ),
        href=url,
        is_external=True,
    )


def hero_section() -> rx.Component:
    """The hero section."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "KEITUMETSE PRECIOUS LEFASO",
                    class_name="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl lg:text-7xl bg-clip-text text-transparent bg-gradient-to-r from-sky-400 to-blue-600",
                ),
                rx.el.p(
                    "Aspiring Cloud Professional | Tech Enthusiast",
                    class_name="mx-auto max-w-[600px] text-slate-500 md:text-xl dark:text-slate-400 mt-4",
                ),
                rx.el.div(
                    hero_button(
                        "Connect on Linkedin",
                        "https://www.linkedin.com/in/keitumetseplefaso",
                        "linkedin",
                    ),
                    hero_button(
                        "Request Resume",
                        "mailto:precious.lefaso@gmail.com",
                        "file-text",
                    ),
                    class_name="mt-8 flex justify-center gap-4",
                ),
                class_name="flex flex-col items-center space-y-4 text-center",
            ),
            class_name="container px-4 md:px-6",
        ),
        id="home",
        class_name="w-full py-20 md:py-32 lg:py-40 flex items-center justify-center",
    )