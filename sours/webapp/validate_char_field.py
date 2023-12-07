def task_validate(description, status, date_of_completion):
    errors = {}
    if not description:
        errors['description'] = 'Обязательно'
    elif len(description) > 60:
        errors['description'] = 'превышает'

    if not status:
        errors['status'] = 'Обязательно'

    if not date_of_completion:
        errors['date_of_completion'] = 'Обязательно'

    return errors

