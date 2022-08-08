unsorted_file = 'F:/sumanth/Python-Code/Python Section1/animal.txt'
sorted_file_name = 'F:/sumanth/Python-Code/Python Section1/animals_sorted_file.txt'
animals = []

try:
    with open(unsorted_file) as file:
        for ani in file:
            animals.append(ani)
        animals.sort()

    print(animals)
except:
    print('Could not open {}.'.format(unsorted_file))


try:
    with open(sorted_file_name, 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('Could not open {}.'.format(sorted_file_name))
