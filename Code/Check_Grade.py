class CheckGrade(object):


    def user_choice(self):
        mark = input("Enter the mark of the student: ")
        while (CheckGrade.is_input_valid(CheckGrade, mark)) == False:
            mark = input("Enter a mark between 0 to 100: ")
        else:
            print("Your grade is:", CheckGrade.get_grade(CheckGrade, mark))
        return mark


    def isfloat(self, mark):
        try:
            float(mark)
            return True
        except ValueError:
            return False


    def is_input_valid(self, mark):
        if CheckGrade.isfloat(CheckGrade, mark):
            mark = float(mark)
            if mark >= 0 and mark <= 100:
                return True
        return False


    def get_grade(self, mark):
        mark = float(mark)
        if mark >= 84.5:
            grade = "HD"
        elif mark >= 74.5 and mark < 84.5:
            grade = "D"
        elif mark >= 64.5 and mark < 74.5:
            grade = "C"
        elif mark >= 49.5 and mark < 64.5:
            grade = "P"
        else:
            grade = "F"

        return grade


def main():
    '''main method'''
    result = CheckGrade()
    result.user_choice()


if __name__ == "__main__":
    main()



