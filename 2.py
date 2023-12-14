file_path = r'C:\Users\Slivkoff_Nathaniel\Downloads\Sample_Data_Age.csv'
output_file_path = r'C:\Users\Slivkoff_Nathaniel\Downloads\Older_Than_65.csv'
output_file_path2 = r'C:\Users\Slivkoff_Nathaniel\Downloads\Alphabetical.csv'

with open(file_path, 'r') as file, open(output_file_path, 'w') as output_file_65:
    for line in file:
        name, age = line.strip().split(',')
        age = int(age)
        
        if age >= 65:
            output_file_65.write(f"{name},{age}\n")

all_people = []
with open(file_path, 'r') as file:
    for line in file:
        name, age = line.strip().split(',')
        age = int(age)
        all_people.append((name, age))

all_people.sort(key=lambda x: x[0])

with open(output_file_path2, 'w') as output_file_alpha:
    for person in all_people:
        output_file_alpha.write(f"{person[0]},{person[1]}\n")