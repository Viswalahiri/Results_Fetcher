def student_list(pass_year,section_number):
  if(pass_year == 2021 or pass_year == 2022):
            if(pass_year == 2021):
                first_string = '1217103'
                max_students = {1 : 64, 2 : 66, 3 : 63, 4 : 66, 5 : 63, 6 : 63, 7 : 63, 8 : 64, 9 : 64, 10 : 62, 11 : 63, 12 : 66, 13 : 61, 14 : 63, 15 : 62, 16 : 64, 17 : 63, 18 : 64, 19 : 60}
                if int(section_number) not in max_students:
                    print("Section " + str(section_number) + " does not exist.")
                    quit()
            if(pass_year == 2022):
                first_string = '1218103'
                max_students = {1 : 62, 2 : 62, 3 : 62, 4 : 63, 5 : 64, 6 : 64, 7 : 64, 8 : 65, 9 : 63, 10 : 64, 11 : 63, 12 : 63, 13 : 63, 14 : 62, 15 : 62, 16 : 62, 17 : 51, 18 : 63}
                if int(section_number) not in max_students:
                    print("Section " + str(section_number) + " does not exist.")
                    quit()
            if(section_number<10):
                first_string = first_string + '0'+ str(int(section_number)) + '001'
            else:
                first_string = first_string + str(int(section_number)) + '001'
            last_string = first_string[0:-2] + str(max_students[int(section_number)])

            first_number = int(first_string)
            last_number = int(last_string)
            class_list = []
            for i in range(first_number,last_number+1):
                class_list.append(str(i))
            return class_list
