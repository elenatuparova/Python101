import csv
import re

def load_data_from_file(file_name):
    all_data = []
    with open('example_data.csv', newline='') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            all_data.append(row)
    fields = all_data[0]
    all_data.pop(0)
    return [fields, all_data]

def validate_filters(file_name, **filters):
    fields, all_data = load_data_from_file(file_name)

    postfixes = ['', 'startswith', 'contains', 'gt', 'lt']

    filter_values = [value for value in filters.values()]

    filter_key_words = [k.split('__') for k in filters.keys()]

    for key_word in filter_key_words:
        if len(key_word) == 1:
            key_word.append('')
        if key_word[0] not in fields and key_word[0] != 'order_by' or key_word[1] not in postfixes:
            raise Exception('Filters must be existing fields!')

    filters_and_values = {}
    for index, key_word in enumerate(filter_key_words):
        if key_word[0] != 'order_by':
            filters_and_values[(fields.index(key_word[0]), key_word[1])] = filter_values[index]
        else:
            if filter_values[index] not in fields:
                raise Exception('Filters must be existing fields!')
            filters_and_values[(key_word[0], key_word[1])] = fields.index(filter_values[index])

    return [all_data, filters_and_values]


def filter_by_criteria(record, field_number, filter_parameter, criteria):
    in_filter = True
    if filter_parameter == '':
        if record[field_number] != str(criteria):
            in_filter = False

    if filter_parameter == 'startswith':
        if re.match(criteria + '.*', record[field_number]) == None:
            in_filter = False

    if filter_parameter == 'contains':
        if criteria not in record[field_number]:
            in_filter = False

    if filter_parameter == 'gt':
        if isinstance(criteria, str):
            if record[field_number] <= criteria:
                in_filter = False
        if isinstance(criteria, int):
            if int(record[field_number]) <= criteria:
                in_filter = False

    if filter_parameter == 'lt':
        if isinstance(criteria, str):
            if record[field_number] >= criteria:
                in_filter = False
        if isinstance(criteria, int):
            if int(record[field_number]) >= criteria:
                in_filter = False

    return in_filter

def order_by_criteria(records, field_number):
    if field_number == 5:
        return sorted(records, key=lambda record: int(record[field_number]))
    return sorted(records, key=lambda record: record[field_number])

def filter(file_name, **filters):
    all_data, filters_and_values = validate_filters(file_name, **filters)

    data_filtered = []
    for record in all_data:
        in_filter = True
        for filter_key, filter_value in filters_and_values.items():
            if filter_key[0] != 'order_by':
                if not filter_by_criteria(record, filter_key[0], filter_key[1], filter_value):
                    in_filter = False
                    break
        if in_filter == True:
            data_filtered.append(record)
        if ('order_by', '') in filters_and_values.keys():
            data_filtered = order_by_criteria(data_filtered, filters_and_values[('order_by', '')])
    return data_filtered

def count(file_name, **filters):
    all_data, filters_and_values = validate_filters(file_name, **filters)
    
    count_filtered = 0
    for record in all_data:
        in_filter = True
        for filter_key, filter_value in filters_and_values.items():
            if filter_key[0] != 'order_by':
                if not filter_by_criteria(record, filter_key[0], filter_key[1], filter_value):
                    in_filter = False
                    break
        if in_filter == True:
            count_filtered += 1
    return count_filtered

def first(file_name, **filters):
    return filter(file_name, **filters)[0]

def last(file_name, **filters):
    return filter(file_name, **filters)[-1]