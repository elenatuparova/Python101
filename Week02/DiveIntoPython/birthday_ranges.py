def birthday_ranges(birthdays, ranges):
    birthdays_in_range = []

    birthdays_count = 0
    for r in ranges:
        for birthday in birthdays:
            if birthday in range(r[0], r[1] + 1):
                birthdays_count += 1
        birthdays_in_range.append(birthdays_count)
        birthdays_count = 0

    return birthdays_in_range