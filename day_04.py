''' Day 4: Secure Container '''
from itertools import groupby


def consecutive_duplicate(digits, **kwargs):
    ''' Checks for consecutive duplicate digits '''
    count_duplicates = [len(list(group)) for _, group in groupby(digits)]
    if 2 in count_duplicates and kwargs.get('double_only'):
        return True
    if any(x > 1 for x in count_duplicates) and not kwargs.get('double_only'):
        return True
    return False


def digit_increase(digits):
    ''' Checks that digits never decreases '''
    i = 0
    while i < len(digits) - 1:
        if digits[i] > digits[i + 1]:
            return False
        i += 1
    return True


def crack_password(tuple_range, **kwargs):
    ''' Brute force the password '''
    valid_numbers = list()
    for number in range(tuple_range[0], tuple_range[1] + 1):
        digit_list = [int(i) for i in str(number)]
        if not consecutive_duplicate(digit_list,
                                     double_only=kwargs.get('double_only')):
            continue

        if not digit_increase(digit_list):
            continue

        valid_numbers.append(number)
    return valid_numbers


PASSWORD_RANGE = 138241, 674034
print(len(crack_password(PASSWORD_RANGE, double_only=True)))
