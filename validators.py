"""Input checking helpers for the command-line program."""


def clean_text(value, field_name):
    value = value.strip()
    if not value:
        raise ValueError(field_name + " cannot be empty.")
    return value


def positive_integer(value, field_name="task number"):
    try:
        number = int(value)
    except ValueError:
        raise ValueError("Enter a whole number for " + field_name + ".")
    if number <= 0:
        raise ValueError(field_name + " must be greater than zero.")
    return number
