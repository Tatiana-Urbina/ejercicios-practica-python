def main(): 
    student = get_student()
    if student[0] == "Roberto":
        student[1]= "San Vicente"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()