import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "age", "contact_number", "E-mail_ID"])
        writer.writerow(info_list)
if __name__ == '__main__':
    input("welcome to student database file")
    condition = True
    student_num = 1
    while condition:
        student_info = input("Enter student information for student #{} (Name age contact_number E-mail_ID):\n".format(student_num))

        student_info_list = student_info.split(' ')
        print("\nThe entered information is -\nname: {}\nage: {}\ncontact_number: {}\nE-mail_ID: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check = input("Is the entered value is correct (yes/no):\n")
        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("Do you want to enter another student information (yes/no):\n").lower()
            if condition_check == "yes":
                condition = True
                student_num += 1
            else:
                condition = False
        else:
            print("\nPlease write the correct information")


