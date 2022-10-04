from django.core.exceptions import ValidationError

'''
1. Unit tests -> concrete isolated piеce of code
2. Integration tests -> integration of coupled pieces of code
3. API test -> Check if the API works correctly
    - Check if the result of HTTP call return the correct JSON
4. Functional/E2E/UI tests - 
'''

'''
Unit tests
'''


def greater_than_zero_validator(value):
    if value <= 0:
        raise ValidationError('Value must be greater than 0!')


'''
- check for negative value - Error
- check for 0 value        - Error
- check for positive value - True
'''


def get_only_positive_values(values):
    positive_values = []
    for value in values:
        try:
            greater_than_zero_validator(value)
            positive_values.append(value)
        except:
            pass

    return positive_values


'''
# With unit tests:
Mock greater_than_zero_validator
- check for empty list
- check for list with positives
- check for list with negatives

# With integration tests:
- No mocking
- [] => []
- [1, 2, 3] => [1, 2, 3]
- [0, 1, 2] => [1, 2]
- [0, 0, 0] => []
- [....
'''

