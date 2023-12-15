import csv
import os

# Function that a CSV file and returns its header and data
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        # Reads the header row
        header = next(reader)
        # Reads each row of dat  
        for row in reader:  
            data.append(row)
    return header, data

# Function to write data to a CSV file
def write_csv(file_name, header, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # Writes the header
        writer.writerow(header)  
        # Writes the data rows
        writer.writerows(data)  

# Function to count people over 64 years old and gather their data
def count_people_over_64(data):
    count = 0
    over_65 = []
    for row in data:
         # Check if age in the row is over 64
        if int(row[1]) > 64:
            # Count of people over 64 
            count += 1  
             # Append their data to a list
            over_65.append(row) 
    return count, over_65

# Function to create a new CSV file with data sorted alphabetically by name
def create_alpha_sorted_csv(data):
    # Sort the data by name (first column)
    sorted_data = sorted(data, key=lambda x: x[0])  
    # Write the sorted data to a new CSV file in the Documents folder
    write_csv(os.path.join(os.path.expanduser('~'), 'Documents', 'alpha_all.csv'), ['Name', 'Age'], sorted_data)

# Function to count people in different age groups
def count_age_groups(data):
    age_groups = {'18-24': 0, '25-35': 0, '36-55': 0, 'Over 55': 0}
    for row in data:
        # Get the age from each row
        age = int(row[1])  
        # Categorize people into different age groups
        if 18 <= age <= 24:
            age_groups['18-24'] += 1
        elif 25 <= age <= 35:
            age_groups['25-35'] += 1
        elif 36 <= age <= 55:
            age_groups['36-55'] += 1
        else:
            age_groups['Over 55'] += 1
    return age_groups

# Function to write age group counts to a CSV file
def write_age_groups_csv(age_groups):
    # Write the age group counts to a new CSV file in the Documents folder
    with open(os.path.join(os.path.expanduser('~'), 'Documents', 'age_data.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
         # Write the header
        writer.writerow(['Age Group', 'Number of People']) 
        for group, count in age_groups.items():
             # Write each age group count
            writer.writerow([group, count]) 

# Main function to orchestrate the process
def main():
    # Set the path to the file in the Downloads folder
    file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'Sample_Data_Age.csv')

    # Read data from the original CSV
    header, data = read_csv(file_path)

    # Count people over 64 and create a new CSV with their data
    count_over_64, over_65_data = count_people_over_64(data)
    print(f'Number of people over 64: {count_over_64}')
    write_csv('over_65.csv', header, over_65_data)

    # Create an alphabetically sorted CSV in the Documents folder
    create_alpha_sorted_csv(data)

    # Count age groups and write the counts to age_data.csv in the Documents folder
    age_groups = count_age_groups(data)
    write_age_groups_csv(age_groups)

# Entry point to start the script
if __name__ == "__main__":
    main()
