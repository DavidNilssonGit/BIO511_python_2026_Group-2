'''
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")


book1 = Book("1984", "George Orwell", 1949)
book1.display()

book2 = Book("Dystopian", "George Orwell", 1949)
book2.display()

book3 = Book("cooking", "Georgia", 1947)
book2.display()

'''

class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def details(self):
        return f"{self.name}, Age: {self.age}"

Patient1 = Patient("445678", "Ana", "56")
print(Patient1.details())

Patient2 = Patient("445648", "Ara", "69")
print(Patient2.details())
