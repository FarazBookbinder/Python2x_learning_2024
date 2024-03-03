from abc import ABC, abstractmethod


class ATB(ABC):
    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass


class Perform(ATB):
    def perform_task1(self):
        print("It's Task 1")


    def perform_task2(self):
        print("It's Task 2")


obj1 = Perform()
obj1.perform_task1()
obj1.perform_task2()
