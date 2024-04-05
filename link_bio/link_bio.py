"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.component.navbar import navbar


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        navbar(),
        navbar()
    )


app = rx.App()
app.add_page(index)
