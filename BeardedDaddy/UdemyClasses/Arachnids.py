scorpions = {'emperor', 'red claw', 'arizona', 'forest', 'fat tail'}

snakes = {'python', 'cobra', 'viper', 'anaconda', 'mamba'}

spiders = {'tarantula', 'black widow', 'wolf spider', 'crab spider'}

vespas = {'yellowjacket', 'hornet', 'paper wasp'}

things_that_bite = {'snakes'}
things_that_sting = scorpions | spiders | vespas
arachnids = spiders | scorpions

# print(arachnids)
# print(things_that_bite)
print(things_that_sting)
