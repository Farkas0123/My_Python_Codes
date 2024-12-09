#### Implementation of the procedural task in Python


# File to store student records
file_name = "student_records.txt"

# Function to save student records to the text file
def save_records(records):
    with open(file_name, 'w') as f:
        for i in records:
            f.write(f'{i[0]};{i[1]};{i[2]};{i[3]}\n')

# Function to load student records from the text file
def load_records():
    result = []
    with open(file_name) as f:
        l = f.readlines()
        for i in l:
            akt = i.split(',')
            result.append([akt[0], akt[1], akt[2], akt[3].strip('\n')])
    return result

# Function to create a new student record
def add_student():
    Name = input('Name = ')
    Id = int(input('Id = '))
    MathScore = int(input('MathScore = '))
    HistoryScore = int(input('HistoryScore = ')) 
    return [Name,Id,'math:'+str(MathScore),'history:'+str(HistoryScore)]

# Function to display all student records
def view_students(records):
    for i in records:
        print(i)

# Function to update a student's exam scores
def update_student(records):
    result = list(records)
    id = int(input('Please enter the ID of the student: '))
    idlist = list(map(lambda x : int(x[1]), result))
    if id in idlist:
        math = int(input('New MathScore = '))
        history = int(input('New HistoryScore = '))
        for i in range(len(result)):
            if int(result[i][1]) == int(id):
                result[i][2] = 'math:'+str(math)
                result[i][3] = 'history:'+str(history)
    else:
        print('No student with this ID')
        pass

    return result
        
# Function to delete a student record
def delete_student(records):
    result = []
    id = int(input('Enter the ID of the student = '))
    idlist = list(map(lambda x : int(x[1]), records))
    if id in idlist:
        for i in range(len(records)):
            if id != int(records[i][1]):
                result.append(records[i])
    return result
    

# Main menu function
def main():
    records = load_records()
    print(list(map(lambda x : int(x[1]), records)))
    while True:
        print("\nMenu:")
        print("1. Add a new student record")
        print("2. View all student records")
        print("3. Update an existing student's scores")
        print("4. Delete a student record")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            records.append(add_student())
        elif choice == "2":
            view_students(records)
        elif choice == "3":
            records = update_student(records)
        elif choice == "4":
            records = delete_student(records)
        elif choice == "5":
            save_records(records)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
