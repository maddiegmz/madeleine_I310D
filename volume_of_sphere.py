def calculate_volume_of_sphere(radius):
    pi = 3.14
    volume = (4/3) * radius * radius * radius * pi
    return volume

radius_1 = 30
volume_1 = calculate_volume_of_sphere(radius_1)
print(f"The volume of the sphere with radius {radius_1} is: {volume_1}")

radius_2 = 40
volume_2 = calculate_volume_of_sphere(radius_2)
print(f"The volume of the sphere with radius {radius_2} is: {volume_2}")
