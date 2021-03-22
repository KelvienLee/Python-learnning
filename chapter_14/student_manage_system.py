class Student(object):
    student_num = 0
    def add_student(self, student_info):
        with open('student.txt', 'a', encoding='utf-8') as file:
            file.write(student_info+'\n')
        return '添加成功'

    def get_student_info(self, student_num):
        with open('student.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if student_num == line[0:5]:
                    result = line
                    break
            else:
                result = '学号不存在'
            return result

    def get_all_student_info(self):
        with open('student.txt', 'r', encoding='utf-8') as file:
            result = file.read()
        return result

    def delete_student(self, student_num):
        if not self.is_student_exists(student_num):
            return '该学号不存在'
        with open('student.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open('student.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                if line[0:5] == student_num:
                    continue
                file.write(line)
        return '删除成功'

    def edit_student(self, student_num):
        if not self.is_student_exists(student_num):
            return '该学号不存在'
        with open('student.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open('student.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                if line[0:5] == student_num:
                    name = input('请输入学生姓名:')
                    gender = input('请输入学生性别：')
                    phone = input('请输入学生电话号码：')
                    student_info = ','.join([student_num, name, gender, phone])
                    file.write(student_info+'\n')
                else:
                    file.write(line)
        return '修改成功'

    def is_student_exists(self, student_num):
        with open('student.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if student_num == line[0:5]:
                    return True
            else:
                return False

    def create_student_num(self):
        if self.student_num == 0:
            try:
                with open('student.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    last_line = lines[-1]
                if last_line:
                    self.student_num = int(last_line.split(',')[0]) + 1
                else:
                    self.student_num = 10001
            except:
                self.student_num = 10001
        else:
            self.student_num += 1
        return str(self.student_num)


def show_message():
    print('------------------------------')
    print('        学生管理系统 v1.0')
    print('                              ')
    print('        1. 添加学生')
    print('        2. 查询学生')
    print('        3. 显示所有学生')
    print('        4. 删除学生')
    print('        5. 修改学生')
    print('        0: 退出系统')
    print('                              ')
    print('------------------------------')




def main():
    student = Student()
    show_message()
    while True:
        try:
            number = int(input('请输入您的选择：'))
        except:
            print('输入的数字无效，请按照提示输入相应数字。')
        else:
            if number == 1:
                student_num = student.create_student_num()
                name = input('请输入要录入的学生姓名：')
                gender = input('请输入学生性别：')
                phone = input('请输入学生的手机号码：')
                student_info = ','.join([student_num, name, gender, phone])
                result = student.add_student(student_info)
                print(result)
            elif number == 2:
                student_num = input('请输入要查询的学生号:')
                result = student.get_student_info(student_num)
                print(result)
            elif number == 3:
                result = student.get_all_student_info()
                print(result)
            elif number == 4:
                student_num = input('请输入要删除的学生号:')
                confirm = input('确认删除请输入y/yes:')
                if confirm == 'y' or confirm == 'yes':
                    result = student.delete_student(student_num)
                    print(result)
                else:
                    print('取消删除')
            elif number == 5:
                student_num = (input('请输入学生号:'))
                result = student.edit_student(student_num)
                print(result)
            elif number == 0:
                print('退出成功!')
                break
            else:
                print('输入无效，请按照提示输入相应数字')


if __name__ == "__main__":
    main()

