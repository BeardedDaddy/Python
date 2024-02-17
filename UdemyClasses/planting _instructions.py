"""
The code above will imort from the module data.py the PLANTS_LIST.
"""
from DATA import PLANTS_LIST

# with open("PLANTING_INSTRUCTIONS.txt", 'w', encoding='utf-8') as output_file:
#     for plant in PLANTS_LIST:
#         # WHERE_TO_PLANT = 'window box' if plant.lifecycle == 'Perennial' else 'garden'  # noqa
#         if plant.lifecycle == 'Perennial':
#             WHERE_TO_PLANT = 'window box'
#         else:
#             WHERE_TO_PLANT = 'garden'
            
with open("PLANTING_INSTRUCTIONS.txt", 'w', encoding='utf-8') as output_file:
    for plant in PLANTS_LIST:
        WHERE_TO_PLANT, who = ('window box', 'me') if plant.lifecycle == 'Perinnial' else ('garden', 'gardner')
        # if plant.lifecycle == 'Perennial':
        #     WHERE_TO_PLANT = 'window box'
        #     who = 'me'
            
        # else:
        #     WHERE_TO_PLANT = 'garden'
        #     who = 'gardener'
            
        print(f"{plant.name}: {WHERE_TO_PLANT}, {who}", file=output_file)
