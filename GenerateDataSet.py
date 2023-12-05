import random

def generate_data_set(size):
    number_of_subset= random.randint(size//2, size)
    subsets = [list(range(i+1, i+random.randint(1, min(5, size//2))+1)) for i in range(number_of_subset)]
    costs = [random.randint(1,100) for i in range(number_of_subset)]
    return size, subsets, costs


def saveFile(file_name, size, sublist, costlist):
    with open(f'DataSet_{file_name}.txt', 'w') as file:
        file.write(f'{size}\n')
        for sub in sublist:
            line_string = ' '.join(map(str, sub))
            file.write(f'{line_string}\n')
        line_cost = ' '.join(map(str, costlist))
        file.write(f'{line_cost}')

if __name__== '__main__':
    scale = [20, 200, 2000]
    
    for data in scale:
        if data == 20:
          name_file = "Small"
        elif data == 200:
          name_file = "Medium"
        else:
           name_file = "Large"
        
        size, subsets, costs = generate_data_set(data)
        saveFile(name_file, size,subsets,costs)