import reflex as rx


def education_item(title: str, institution: str, date: str) -> rx.Component:
    """An item in the education section."""
    return rx.el.div(
        rx.el.div(
            rx.icon("graduation-cap", class_name="h-8 w-8 text-sky-500"),
            class_name="flex-shrink-0",
        ),
        rx.el.div(
            rx.el.h3(
                title, class_name="text-lg font-semibold text-slate-900 dark:text-white"
            ),
            rx.el.p(
                institution, class_name="text-sm text-slate-600 dark:text-slate-400"
            ),
            rx.el.p(date, class_name="text-xs text-slate-500 dark:text-slate-500"),
            class_name="ml-4",
        ),
        class_name="flex items-start p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-100 dark:border-slate-800",
    )


def education_section() -> rx.Component:
    """The education section."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Education & Certifications",
                class_name="text-3xl font-bold tracking-tighter sm:text-4xl text-center",
            ),
            rx.el.div(
                education_item(
                    "Bsc Information Systems and Data Management",
                    "University of Botswana",
                    "2016-2020",
                ),
                education_item(
                    "AWS Certified Cloud Practitioner",
                    "Amazon Web Services",
                    "2025 (Planned)",
                ),
                class_name="mt-8 grid max-w-2xl mx-auto gap-6",
            ),
            class_name="container px-4 md:px-6",
        ),
        id="education",
        class_name="w-full py-12 md:py-24 lg:py-32 bg-slate-100 dark:bg-slate-900/50",
    )