alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_inc = 1
elif alien_0['speed'] == 'medium':
    x_inc = 2
else:
    x_inc = 3

alien_0['x_position'] = alien_0['x_position'] + x_inc

print(f"New position: {alien_0['x_position']}")

