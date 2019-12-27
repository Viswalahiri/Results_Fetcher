import os
import student_list
import browser_connect
import select_fields
def main():
  print("Enter semester, batch year, and section number.")
  semester,batch_year,section_number = [int(i) for i in input().split()]
  class_list = student_list.student_list(batch_year,section_number)
  driver = browser_connect.browser_connect()
  select_fields.select_fields(batch_year, semester,driver,class_list, section_number)

if __name__ == "__main__":
    main()
