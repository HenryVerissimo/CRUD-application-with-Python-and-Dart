import re


def validate_email(email: str) -> bool:
    """This function validates any icoming email with a regex pattern.

    Args:
        email(str): The email to validated.

    Returns:
        bool: True if email is valid or False if not.

    Examples:

        >>> validate_email("Henry@gmail.com")
        True
        >>> validate_email("Rafaplayer@hotmail.com)
        True
        >>> validate_email("Bia!#$@hotmail.com)
        False
    """

    regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # nosec

    if re.fullmatch(regex_email, email):
        return True

    return False


def validate_password(password: str) -> bool:
    """This function validates any incoming password with a regex pattern.

    Args:
        password(str): The password to validated.

    Returns:
        bool: True if password is valid or False if not.

    Examples:
        >>> validate_password(SECRETpass3457$@)
        True
        >>> validate_password(password123)
        False
        >>> validate_password(HENRY55)
        False
    """

    regex_password = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"  # nosec
    )

    if re.fullmatch(regex_password, password):
        return True

    return False


def validate_username(username: str) -> bool:
    """This function validates any incoming username with a regex pattern.

    Args:
        username(str): The username to validated.

    Returns:
        bool: True if username is valid or False if not.

    Examples:
        >>> validated_username(Henry_22)
        True
        >>> validated_username(Bia)
        False
        >>> validated_username(Rafa!!!#)
        False
    """

    regex_username = r"^[\w\-\.]{4,20}$"  # nosec

    if re.fullmatch(regex_username, username):
        return True

    return False
