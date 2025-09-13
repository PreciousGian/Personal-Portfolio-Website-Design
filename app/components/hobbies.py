import reflex as rx


def hobby_card(icon: str, title: str) -> rx.Component:
    """A card for a hobby."""
    return rx.el.div(
        rx.el.div(rx.el.p(icon, class_name="text-4xl"), class_name="mb-4"),
        rx.el.h3(
            title, class_name="text-lg font-semibold text-slate-900 dark:text-white"
        ),
        class_name="flex flex-col items-center justify-center p-6 bg-white dark:bg-slate-900 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-800 hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def hobbies_section() -> rx.Component:
    """The hobbies section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Hobbies & Interests",
                class_name="text-3xl font-bold tracking-tighter sm:text-4xl text-center",
            ),
            rx.el.div(
                hobby_card("📖", "Reading"),
                hobby_card("⚽", "Football"),
                hobby_card("🎮", "Gaming"),
                hobby_card("✈️", "Traveling"),
                class_name="mt-8 grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6",
            ),
            class_name="container px-4 md:px-6",
        ),
        id="hobbies",
        class_name="w-full py-12 md:py-24 lg:py-32",
    )