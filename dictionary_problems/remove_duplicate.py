result = {}


def remove_duplicate_value(data):
    for key, value in data.items():
        if value not in result.values():
            result[key] = value
    return result


data = {
    'id1': {
        'name': 'saurabh', 'class': 'VI'},
    'id2': {
        'name': 'Abhijeet', 'class': 'VII'},
    'id3': {
        'name': 'Saa', 'class': 'IX'},
    'id4': {
        'name': 'saurabh', 'class': 'VI'}
}
print(remove_duplicate_value(data))