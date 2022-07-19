favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }
# sort the sets by showing the items that are just in the favourites and not in the baskets.
# I used the the difference method.
suggestions = favourites - basket
print(suggestions)
