# utils.py


# function to format phone number
def format_phone_number(phone_number):
    """
    Format a phone number to have the correct country code and format.

    Args:
        phone_number (str): The phone number to format.

    Returns:
        str: The formatted phone number.
    """
    phone_number = phone_number.strip()  # Remove leading and trailing whitespaces
    phone_number = phone_number.replace(" ", "")
    phone_number = phone_number.replace("-", "")
    phone_number = phone_number.replace("(", "")
    phone_number = phone_number.replace(")", "")
    phone_number = phone_number.replace("+", "")
    try:
        if phone_number.startswith("0") and len(phone_number) == 10:
            phone_number = f"+233{phone_number[1:]}"  # Add country code for Ghana
        elif phone_number.startswith("233") and len(phone_number) == 12:
            phone_number = f"+{phone_number}"  # Add '+' sign if missing
        return phone_number
    except ValueError:
        return None  # Return None if there is an error
