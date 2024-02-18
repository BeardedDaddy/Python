"""
The code above will import from the module data.py the PLANTS_LIST.
"""
try:
    from data import plants_list
except ImportError:
    plants_list = []  # Define PLANTS_LIST if it doesn't exist in the data module  # noqa

# with open("PLANTING_INSTRUCTIONS.txt", 'w', encoding='utf-8') as output_file:
#     for plant in PLANTS_LIST:
#         # WHERE_TO_PLANT = 'window box' if plant.lifecycle == 'Perennial' else 'garden'  # noqa
#         if plant.lifecycle == 'Perennial':
#             WHERE_TO_PLANT = 'window box'
#         else:
#             WHERE_TO_PLANT = 'garden'


def sort_perinnials(item) -> str:
    if item.lifecycle.casefold() == 'perinnial':
        return '1' + item.name
    else:
        return '0' + item.name


# plants_list.sort(key=sort_perinnials)
plants_list.sort(key=lambda item: '1' + item.name if item.lifecycle ==
                 'Perinnial' else '0' + item.name)

with open("planting_instructions.txt", 'w', encoding='utf-8') as output_file:
    for plant in plants_list:
        WHERE_TO_PLANT, who = ('window box', 'me') if plant.lifecycle == 'Perinnial' else ('garden', 'gardner')  # noqa
        # if plant.lifecycle == 'Perennial':
        #     WHERE_TO_PLANT = 'window box'
        #     who = 'me'

        # else:
        #     WHERE_TO_PLANT = 'garden'
        #     who = 'gardener'

        print(f"{plant.name}: {WHERE_TO_PLANT}, {who}", file=output_file)
