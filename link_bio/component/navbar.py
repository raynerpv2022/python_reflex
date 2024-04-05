import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("Resbaloso",
                color="black",
                height="40px",
                ),
                bg="yellow",
                position="sticky",
                padding_x = "16px",
                padding_y= "8px",
                z_index="999"

    )