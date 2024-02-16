from medals_data import medals_table


def sort_key(d: dict, field: str) -> str:
    return d['field']


medals_table.sort(key=sort_key)
print(medals_table)
