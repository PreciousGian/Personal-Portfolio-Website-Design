import reflex as rx
from app.state import PortfolioState
from app.components.navbar import navbar
from app.components.hero import hero_section
from app.components.education import education_section
from app.components.hobbies import hobbies_section
from app.components.contact import contact_section
from app.components.footer import footer


def index() -> rx.Component:
    """The main page of the portfolio."""
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero_section(),
            education_section(),
            hobbies_section(),
            contact_section(),
            class_name="pt-16",
        ),
        footer(),
        class_name=PortfolioState.theme_class,
    )


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="sky"),
    style={
        "background_image": "url(/background.png)",
        "background_size": "cover",
        "background_position": "center",
        "background_attachment": "fixed",
    },
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
    stylesheets=["/styles.css"],
)
app.add_page(index, title="Keitumetse Lefaso | Portfolio")