def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_valid_account_number(account_number):
    return account_number.isdigit() and len(account_number) == 10
