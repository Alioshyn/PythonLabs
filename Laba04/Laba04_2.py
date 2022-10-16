# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический).
# Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.
# ДОБАВИТЬ МЕТОДЫ КЛАССА И СТАТИЧЕСКИЕ МЕТОДЫ.
# Вар.2
# Kласс Abiturient: id, Фамилия, Имя, Отчество, Адрес, Телефон, Оценки.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов.
# Вывести:
# a)	список абитуриентов, имеющих неудовлетворительные оценки;
# б) список абитуриентов, у которых сумма баллов выше заданной;

class Abiturient:
    abiturient_list = []

    def get_student_id(self):
        return self.__student_id


    def set_student_id(self, student_id):
        if not self.is_student_id_exist(student_id):
            self.__student_id = student_id
        else:
            print('Студент с данным ID уже существует. Выберите другой ID')
            student_id = int(input('Введите ID студента: '))
            self.__student_id = self.set_student_id(student_id)
        return self.get_student_id()


    def is_student_id_exist(self, student_id):
        if Abiturient.get_student_list():
            for i in range(len(Abiturient.abiturient_list)):
                if Abiturient.abiturient_list[i].get_student_id() == student_id:
                    return True
        else:
            return False


    def get_student_lastname(self):
        return self.__student_lastname

    def set_student_lastname(self, student_lastname):
        self.__student_lastname = student_lastname


    def get_student_name(self):
        return self.__student_name

    def set_student_name(self, student_name):
        self.__student_name = student_name


    def get_student_surname(self):
        return self.__student_surname

    def set_student_surname(self, student_surname):
        self.__student_surname = student_surname


    def get_student_address(self):
        return self.__student_address

    def set_student_address(self, student_address):
        self.__student_address = student_address


    def get_student_phone(self):
        return self.__student_phone

    def set_student_phone(self, student_phone):
        self.__student_phone = student_phone


    def get_student_ratings(self):
        return self.__student_ratings

    def set_student_ratings(self, student_ratings):
        self.__student_ratings = student_ratings


    @staticmethod
    def get_student_list():
        return Abiturient.abiturient_list


    @staticmethod
    def add_student_to_list(student):
        Abiturient.abiturient_list.append(student)

    @staticmethod
    def remove_student_from_list(student_id):
        flag = False
        index = 0
        for i in range(len(Abiturient.abiturient_list)):
            if Abiturient.abiturient_list[i].__student_id == student_id:
                index = i
                flag = True
        if flag == 0:
            print(f"Студент с ID {student_id} отсутствует в списке")
        else:
            Abiturient.abiturient_list.pop(index)
            print(f"Студент с ID {student_id} удален из списка")


    @staticmethod
    def print_student_list():
        if Abiturient.abiturient_list:
            for i in range(len(Abiturient.abiturient_list)):
                print(Abiturient.abiturient_list[i])
        else:
            print("Список студентов пуст")

    # @classmethod
    # def find_student_by_bad_ratings(cls, bad_ratings):
    #     pass
    #     checker = 0

#     for i in range(len(cls.book_list)):
#         if author_name.casefold() in cls.book_list[i].book_author.casefold():
#             print(cls.book_list[i])
#             checker = 1
#     if checker == 0:
#         print("\33[31m\033[1m {}".format('Book with Author Name = \'' + author_name + '\' has not been found!'))
#
#
    # @classmethod
    # def find_student_by_sum_ratings(cls, sum_ratings):
    #     checker = 0
    #     for i in range(len(cls.Abiturient.abiturient_list.__student_ratings)):
    #         checker += 1
    #     print(checker)
        #     if cls.book_list[i].__book_year >= year:
        #         print(cls.book_list[i])
        #         checker += 1
        # if checker == 0:
        #     print("\33[31m\033[1m {}".format('No books have been found for provided conditions!'))


    def __str__(self):
        return 'ID студента ' + str(self.__student_id) + \
               '; Фамилия: ' + self.__student_lastname + \
               '; Имя: ' + self.__student_name + \
               '; Отчество = ' + self.__student_surname + \
               '; Адрес = ' + self.__student_address + \
               '; Телефон = ' + self.__student_phone + \
               '; Оценки = ' + str(self.__student_ratings)

def add_new_student():
    student = Abiturient()
    student.set_student_id(int(input('Введите ID студента: ')))
    student.set_student_lastname(input('Введите фамилию: '))
    student.set_student_name(input('Введите имя: '))
    student.set_student_surname(input('Введите отчество: '))
    student.set_student_address(input('Введите адрес: '))
    student.set_student_phone(input('Введите телефон: '))
    student.set_student_ratings(input('Введите оценку: '))
    Abiturient.add_student_to_list(student)
    print("Студент добавлен в список")
    print(student)


option = 1
while option != 0:
    print('\nМеню')
    print('1 - Добавить студента')
    print('2 - Удалить студента')
    print('3 - Список студентов')
    print('4 - Список студентов, имеющих неудовлетворительные оценки')
    print('5 - Список студентов, у которых сумма баллов выше заданной')
    print('0 - Выход')
    option = int(input('\nВыберите нужный пункт: '))
    if option == 1:
        print('Добавление студента')
        add_new_student()
    elif option == 2:
        student_id = int(input('\nВведите Id удаляемого студента: '))
        Abiturient.remove_student_from_list(student_id)
    elif option == 3:
        print('\nСписок студентов: ')
        Abiturient.print_student_list()
    elif option == 4:
        bad_ratings = input('\nВведите неудовлетворительную оценку: ')
#        Abiturient.find_student_by_bad_ratings(bad_ratings)
    elif option == 5:
        print(Abiturient.abiturient_list[0].__student_ratings)
#        sum_ratings = int(input('\nВведите сумму баллов: '))
#        Abiturient.find_student_by_sum_ratings(sum_ratings)
    elif option == 0:
        print("Программа завершена")
        option = 0
    else:
        print("Данный пункт недоступен. Выберите другой")
        continue