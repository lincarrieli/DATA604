import random
colors = 'red','yellow','purple','green','blue','black','orange','white'
picked_color = []
simulations = 1000
for color in colors:
    for i in range(simulations):
        picked_color.append(color)
    
color = random.choice(picked_color)
print(color)