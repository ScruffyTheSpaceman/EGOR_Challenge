import re

def is_valid_credit_card(number):
    """
    Validate the credit card number using regex.
    """
    # Regex for validating a credit card number
    regex = (
        r'^'                                    # start of string
        r'(?!.*(\d)(-?\1){3})'                  # negative lookahead for 4 or more consecutive repeated digits
        r'[456]'                                # starts with 4, 5, or 6
        r'\d{3}'                                # followed by 3 digits
        r'('                                    # start of group for separators
        r'(?:-\d{4}){3}'                        # three groups of four digits, separated by dashes
        r'|'                                    # OR
        r'\d{12}'                               # 12 digits with no dashes
        r')'                                    # end of group for separators
        r'$'                                    # end of string
    )

    return re.fullmatch(regex, number) is not None

# Sample test cases
credit_card_numbers = [
    "4123456789123456",
    "5123-4567-8912-3456",
    "61234-567-8912-3456",
    "4123356789123456",
    "5133-3367-8912-3456",
    "5123 - 3567 - 8912 - 3456"
]

# Check each credit card number using the validation function
validity_checks = {number: is_valid_credit_card(number) for number in credit_card_numbers}
print(validity_checks)
